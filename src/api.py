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


@app.get("/dashboard")
def dashboard_data():

    engine = assistant.engine

    region_sales = (
        engine.total_sales_by_region()
    )

    category_sales = (
        engine.category_performance()
    )

    promotion_uplift = (
        engine.promotion_uplift()
    )

    highest_region = (
        engine.highest_sales_region()
    )

    total_sales = (
        engine.df["sales"].sum()
    )

    return {

        "total_sales": round(
            float(total_sales),
            2
        ),

        "highest_sales_region": (
            highest_region
        ),

        "promotion_uplift": round(
            float(promotion_uplift),
            2
        ),

        "sales_by_region": (
            region_sales
            .round(2)
            .to_dict()
        ),

        "sales_by_category": (
            category_sales
            .round(2)
            .to_dict()
        )
    }