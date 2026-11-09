from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from transformers import pipeline
from langchain_core.runnables import RunnableLambda

# Modelo de tradução inglês -> alemão
MODELO = "Helsinki-NLP/opus-mt-en-de"

app = FastAPI(
    title="API de Tradução Inglês-Alemão",
    description="Tradução com FastAPI, LangChain e Hugging Face",
    version="1.0.0"
)

# Carrega o modelo Hugging Face uma única vez
tradutor_huggingface = pipeline(
    task="text2text-generation",
    model=MODELO,
    device=-1
)

# LangChain gerencia a chamada ao modelo
def traduzir_com_modelo(texto: str) -> str:
    resultado = tradutor_huggingface(texto, max_new_tokens=512)
    return resultado[0]["generated_text"]


cadeia_traducao = RunnableLambda(traduzir_com_modelo)


class TextoEntrada(BaseModel):
    texto: str = Field(min_length=1)


class TextoSaida(BaseModel):
    texto_original: str
    texto_traduzido: str


@app.get("/")
def inicio():
    return {
        "mensagem": "API de tradução inglês-alemão funcionando",
        "modelo": MODELO
    }


@app.post("/traduzir", response_model=TextoSaida)
def traduzir(entrada: TextoEntrada):
    try:
        traducao = cadeia_traducao.invoke(entrada.texto)

        return TextoSaida(
            texto_original=entrada.texto,
            texto_traduzido=traducao
        )

    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Não foi possível realizar a tradução."
        )