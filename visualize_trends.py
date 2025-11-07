"""Example script for visualizing rejection trends over time and companies."""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

from nlp_utils import DATA_PATH, load_data


def main(csv_path: Path = DATA_PATH) -> None:
    df = load_data(csv_path)
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

    monthly = df["Date"].dt.to_period("M").value_counts().sort_index()
    monthly.plot(kind="bar", title="Rejections over time")
    plt.xlabel("Month")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.show()

    df["Company"] = df["Subject"].str.extract(r"Your (\w+)")
    company_counts = df["Company"].dropna().value_counts().head(10)
    company_counts.plot(kind="bar", title="Top rejection sources by company")
    plt.xlabel("Company")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()

