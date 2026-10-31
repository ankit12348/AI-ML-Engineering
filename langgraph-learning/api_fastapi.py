from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="My FastAPI Learning App")


class ChatRequest(BaseModel):
    user_name: str
    message: str


@app.get("/")
def read_root():
    return {"status": "FastAPI server is live and running!"}


@app.post("/interact")
def handle_interaction(request: ChatRequest):
    return {
        "status": "success",
        "greeting": f"Hello {request.user_name}!",
        "processed_message": f"Your message was: '{request.message}'",
    }
