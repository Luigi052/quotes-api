from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import random

app = FastAPI(title="Quotes API", version="1.0.1")

QUOTES = [
    "Keep it simple.",
    "Ship small, ship often.",
    "Automate what hurts.",
    "You build it, you run it.",
    "New quote in version 1.0.1!",
]

class Quote(BaseModel):
    text: str

@app.get("/healthz")
def healthz():
    return {"status": "ok"}

@app.get("/quotes", response_model=List[Quote])
def list_quotes():
    return [{"text": q} for q in QUOTES]

@app.get("/quotes/random", response_model=Quote)
def random_quote():
    return {"text": random.choice(QUOTES)}
