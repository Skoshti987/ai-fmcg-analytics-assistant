from fastapi import FastAPI
from pydantic import BaseModel

from src.main import FMCGAnalyticsAssistant


app = FastAPI(
    title="FMCG AI Analytics Assistant",
    description=(
        "AI-powered business analytics assistant "
        "for FMCG promotion data"
    ),
    version="1.0.0"
)


assistant = FMCGAnalyticsAssistant(
    "data/fmcg_promotions.csv"
)


class QuestionRequest(BaseModel):

    question: str


@app.get("/")
def home():

    return {
        "message": (
            "FMCG AI Analytics Assistant API "
            "is running"
        )
    }


@app.post("/ask")
def ask_question(
    request: QuestionRequest
):

    answer = assistant.answer_question(
        request.question
    )

    return {
        "question": request.question,
        "answer": answer
    }