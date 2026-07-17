class QueryGuardrails:

    ALLOWED_INTENTS = [
        "highest_sales_region",
        "promotion_impact",
        "sales_by_region",
        "category_performance"
    ]

    ALLOWED_REGIONS = [
        "North",
        "South",
        "East",
        "West"
    ]

    def validate(self, parsed_query):

        intent = parsed_query.get("intent")

        # Validate intent
        if intent not in self.ALLOWED_INTENTS:

            return {
                "valid": False,
                "error": "Unsupported analytical operation."
            }

        # Validate region if provided
        region = parsed_query.get("region")

        if region:

            if region not in self.ALLOWED_REGIONS:

                return {
                    "valid": False,
                    "error": "Invalid region specified."
                }

        return {
            "valid": True,
            "error": None
        }