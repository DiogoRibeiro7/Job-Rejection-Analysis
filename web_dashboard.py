from pathlib import Path

import pandas as pd
from nlp_utils import load_data

try:  # pragma: no cover - optional dependency
    import streamlit as st
except Exception:  # pragma: no cover
    st = None

DATA_PATH = Path(__file__).resolve().parent / "data" / "rejections.csv"


def main() -> None:
    """Run the interactive Streamlit dashboard."""
    if st is None:
        raise RuntimeError("streamlit is required to run the dashboard")

    st.title("Job Rejection Dashboard")
    df = load_data(DATA_PATH)
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    st.subheader("Dataset preview")
    st.write(df.head())

    st.subheader("Monthly Rejection Counts")
    monthly = df["Date"].dt.to_period("M").value_counts().sort_index()
    st.bar_chart(monthly)

    st.subheader("Top Companies")
    company_col = None
    for col in df.columns:
        if col.lower() in {"company", "company name"}:
            company_col = col
            break
    if company_col:
        top_companies = df[company_col].value_counts().head(10)
        st.bar_chart(top_companies)
    else:
        st.write("No company column available in dataset.")


if __name__ == "__main__":
    main()
