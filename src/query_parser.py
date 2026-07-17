class QueryParser:

    def parse(self, question):

        question = question.lower().strip()

        region = None

        # Detect region
        for r in ["north", "south", "east", "west"]:

            if r in question:

                region = r.capitalize()

        # Detect time period
        period = None

        if "last month" in question:

            period = "last_month"

        elif "this month" in question:

            period = "this_month"

        elif "last week" in question:

            period = "last_week"

        # Detect intent
        if (
            "highest sales" in question
            or "top region" in question
            or "best region" in question
        ):

            return {
                "intent": "highest_sales_region",
                "region": region,
                "period": period
            }

        elif (
            "promotion" in question
            and (
                "improve" in question
                or "impact" in question
                or "uplift" in question
                or "campaign" in question
            )
        ):

            return {
                "intent": "promotion_impact",
                "region": region,
                "period": period
            }

        elif (
            "sales by region" in question
            or "sales in each region" in question
        ):

            return {
                "intent": "sales_by_region",
                "region": region,
                "period": period
            }

        elif (
            "best category" in question
            or "category performance" in question
            or "highest selling category" in question
        ):

            return {
                "intent": "category_performance",
                "region": region,
                "period": period
            }

        else:

            return {
                "intent": "unknown",
                "region": region,
                "period": period
            }