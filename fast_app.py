import os
import uvicorn
from fastapi import FastAPI
from langserve import add_routes
from dotenv import load_dotenv, find_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate


load_dotenv(find_dotenv())
os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY")

app = FastAPI(
    title="Langchain Server",
    version="0.0.1",
    description="A Simple API Server"
)

@app.get("/")
def home():
    return {"message": "Server is up and running"}

add_routes(
    app,
    ChatOpenAI(),
    path='/openai'
)

model = ChatOpenAI()
prompt = ChatPromptTemplate.from_template("Provide me an essay about {topic}")
prompt1 = ChatPromptTemplate.from_template("Provide me a essay about {topic}")

add_routes(
    app,
    prompt | model,
    path='/essay'

)

add_routes(
    app,
    prompt1 | model,
    path='/poem'

)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)