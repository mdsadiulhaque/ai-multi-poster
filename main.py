from fastapi import FastAPI
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/post")
def create_post(content: str):
    return {"message": "Post created", "content": content}
