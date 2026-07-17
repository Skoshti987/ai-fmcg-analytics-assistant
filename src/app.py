import streamlit as st
import requests
import pandas as pd


st.set_page_config(
    page_title="FMCG AI Analytics Assistant",
    page_icon="📊",
    layout="wide"
)


st.title(
    "📊 FMCG AI Analytics Assistant"
)

st.markdown(
    """
    Explore FMCG sales and promotion performance
    using natural language analytics.
    """
)


API_URL = (
    "http://127.0.0.1:8000"
)


# Dashboard section
st.header(
    "📈 Business Performance Dashboard"
)


try:

    dashboard_response = requests.get(
        f"{API_URL}/dashboard"
    )

    if dashboard_response.status_code == 200:

        data = (
            dashboard_response
            .json()
        )

        col1, col2, col3, col4 = (
            st.columns(4)
        )

        with col1:

            st.metric(
                "Total Sales",
                f"{data['total_sales']:,.0f}"
            )

        with col2:

            st.metric(
                "Top Region",
                data[
                    "highest_sales_region"
                ]
            )

        with col3:

            st.metric(
                "Promotion Uplift",
                f"{data['promotion_uplift']}%"
            )

        with col4:

            st.metric(
                "Data Status",
                "Verified"
            )

        st.divider()

        col1, col2 = (
            st.columns(2)
        )

        with col1:

            st.subheader(
                "Sales by Region"
            )

            region_data = pd.DataFrame(
                {
                    "Region": (
                        list(
                            data[
                                "sales_by_region"
                            ].keys()
                        )
                    ),

                    "Sales": (
                        list(
                            data[
                                "sales_by_region"
                            ].values()
                        )
                    )
                }
            )

            st.bar_chart(
                region_data.set_index(
                    "Region"
                )
            )

        with col2:

            st.subheader(
                "Sales by Category"
            )

            category_data = pd.DataFrame(
                {
                    "Category": (
                        list(
                            data[
                                "sales_by_category"
                            ].keys()
                        )
                    ),

                    "Sales": (
                        list(
                            data[
                                "sales_by_category"
                            ].values()
                        )
                    )
                }
            )

            st.bar_chart(
                category_data.set_index(
                    "Category"
                )
            )

    else:

        st.warning(
            "Dashboard data is unavailable."
        )

except requests.exceptions.ConnectionError:

    st.warning(
        "Start the FastAPI server to load "
        "dashboard data."
    )


st.divider()


# AI Question Section
st.header(
    "🤖 Ask Your Business Question"
)


question = st.text_input(
    "Enter your question",
    placeholder=(
        "Example: Did the South campaign "
        "improve sales last month?"
    )
)


if st.button(
    "Analyze",
    type="primary"
):

    if not question.strip():

        st.warning(
            "Please enter a business question."
        )

    else:

        try:

            response = requests.post(
                f"{API_URL}/ask",

                json={
                    "question": question
                }
            )

            if response.status_code == 200:

                result = (
                    response.json()
                )

                st.success(
                    "Analysis completed successfully"
                )

                st.subheader(
                    "Business Answer"
                )

                st.info(
                    result["answer"]
                )

            else:

                st.error(
                    "The API returned an error."
                )

        except requests.exceptions.ConnectionError:

            st.error(
                "Could not connect to the FastAPI server."
            )