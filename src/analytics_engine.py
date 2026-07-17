import pandas as pd


class FMCGAnalyticsEngine:

    def __init__(self, data_path):
        self.df = pd.read_csv(data_path)
        self.df["date"] = pd.to_datetime(self.df["date"])

    def filter_by_period(self, period):
        """
        Filter the dataset based on the requested time period.
        """

        data = self.df.copy()

        if period == "last_month":

            latest_date = data["date"].max()

            # Get the previous month
            previous_month = latest_date - pd.DateOffset(months=1)

            data = data[
                (data["date"].dt.month == previous_month.month)
                & (data["date"].dt.year == previous_month.year)
            ]

        elif period == "this_month":

            latest_date = data["date"].max()

            data = data[
                (data["date"].dt.month == latest_date.month)
                & (data["date"].dt.year == latest_date.year)
            ]

        elif period == "last_week":

            latest_date = data["date"].max()

            start_date = latest_date - pd.Timedelta(days=13)
            end_date = latest_date - pd.Timedelta(days=7)

            data = data[
                (data["date"] >= start_date)
                & (data["date"] <= end_date)
            ]

        return data

    def total_sales_by_region(self, data=None):

        if data is None:
            data = self.df

        return (
            data.groupby("region")["sales"]
            .sum()
            .sort_values(ascending=False)
        )

    def promotion_impact(self, data=None):

        if data is None:
            data = self.df

        return (
            data.groupby("promotion")["sales"]
            .mean()
        )

    def promotion_uplift(self, data=None):

        if data is None:
            data = self.df

        avg_sales = (
            data.groupby("promotion")["sales"]
            .mean()
        )

        promoted_sales = avg_sales.get("Yes", 0)
        non_promoted_sales = avg_sales.get("No", 0)

        if non_promoted_sales == 0:
            return 0

        uplift = (
            (promoted_sales - non_promoted_sales)
            / non_promoted_sales
        ) * 100

        return round(uplift, 2)

    def promotion_uplift_by_region_and_period(
        self,
        region=None,
        period=None
    ):
        """
        Calculate promotion uplift after applying
        region and time-period filters.
        """

        data = self.df.copy()

        # Apply time-period filter
        if period:
            data = self.filter_by_period(period)

        # Apply region filter
        if region:
            data = data[
                data["region"] == region
            ]

        # Check whether data exists
        if data.empty:
            return 0

        return self.promotion_uplift(data)

    def highest_sales_region(self, data=None):

        if data is None:
            data = self.df

        return (
            data.groupby("region")["sales"]
            .sum()
            .idxmax()
        )

    def category_performance(self, data=None):

        if data is None:
            data = self.df

        return (
            data.groupby("category")["sales"]
            .sum()
            .sort_values(ascending=False)
        )


if __name__ == "__main__":

    engine = FMCGAnalyticsEngine(
        "data/fmcg_promotions.csv"
    )

    print("\n--- TOTAL SALES BY REGION ---")
    print(
        engine.total_sales_by_region()
    )

    print("\n--- OVERALL PROMOTION UPLIFT ---")
    print(
        engine.promotion_uplift(),
        "%"
    )

    print("\n--- SOUTH REGION LAST MONTH UPLIFT ---")
    print(
        engine.promotion_uplift_by_region_and_period(
            region="South",
            period="last_month"
        ),
        "%"
    )

    print("\n--- HIGHEST SALES REGION ---")
    print(
        engine.highest_sales_region()
    )

    print("\n--- CATEGORY PERFORMANCE ---")
    print(
        engine.category_performance()
    )