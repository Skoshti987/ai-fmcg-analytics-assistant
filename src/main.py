from src.query_parser import QueryParser
from src.analytics_engine import FMCGAnalyticsEngine
from src.guardrails import QueryGuardrails


class FMCGAnalyticsAssistant:

    def __init__(self, data_path):

        self.parser = QueryParser()

        self.engine = FMCGAnalyticsEngine(
            data_path
        )

        self.guardrails = QueryGuardrails()

    def answer_question(self, question):

        parsed_query = self.parser.parse(
            question
        )

        print("\nStructured Query:")
        print(parsed_query)

        validation = self.guardrails.validate(
            parsed_query
        )

        if not validation["valid"]:

            return (
                f"Request rejected: "
                f"{validation['error']}"
            )

        intent = parsed_query["intent"]

        region = parsed_query.get(
            "region"
        )

        period = parsed_query.get(
            "period"
        )

        if intent == "highest_sales_region":

            highest_region = (
                self.engine.highest_sales_region()
            )

            return (
                f"The region with the highest "
                f"total sales during the analyzed "
                f"period was {highest_region}."
            )

        elif intent == "promotion_impact":

            uplift = (
                self.engine
                .promotion_uplift_by_region_and_period(
                    region=region,
                    period=period
                )
            )

            if region and period:

                readable_period = (
                    period.replace(
                        "_",
                        " "
                    )
                )

                return (
                    f"For the {region} region during "
                    f"{readable_period}, promoted products "
                    f"generated an average sales uplift "
                    f"of {uplift}% compared with "
                    f"non-promoted products."
                )

            elif region:

                return (
                    f"In the {region} region, promoted "
                    f"products generated an average "
                    f"sales uplift of {uplift}%."
                )

            else:

                return (
                    f"Promoted products generated an "
                    f"average sales uplift of "
                    f"{uplift}%."
                )

        elif intent == "sales_by_region":

            result = (
                self.engine.total_sales_by_region()
            )

            return (
                "Total sales by region:\n"
                f"{result.to_string()}"
            )

        elif intent == "category_performance":

            result = (
                self.engine.category_performance()
            )

            return (
                "Category performance based on "
                f"total sales:\n"
                f"{result.to_string()}"
            )

        else:

            return (
                "I cannot answer that question "
                "using the available analytical tools."
            )


if __name__ == "__main__":

    assistant = FMCGAnalyticsAssistant(
        "data/fmcg_promotions.csv"
    )

    print(
        "\nFMCG AI Analytics Assistant"
    )

    print(
        "=" * 40
    )

    while True:

        question = input(
            "\nAsk your business question "
            "(type 'exit' to quit): "
        )

        if question.lower().strip() == "exit":

            print(
                "Goodbye!"
            )

            break

        answer = (
            assistant.answer_question(
                question
            )
        )

        print(
            "\nAnswer:"
        )

        print(
            answer
        )