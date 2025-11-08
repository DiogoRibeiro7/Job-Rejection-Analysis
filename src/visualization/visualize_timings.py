"""Visualize when rejection emails tend to arrive."""

import argparse
import matplotlib.pyplot as plt

from nlp import load_data


ORDERED_DAYS = ["Mon", "Tues", "Weds", "Thurs", "Fri", "Sat", "Sun"]


def plot_timings(df, prefix: str) -> None:
    """Save bar charts of rejection counts by day and hour."""
    counts = df["Day"].value_counts()
    counts = counts.reindex(ORDERED_DAYS).fillna(0)
    plt.figure(figsize=(6, 4))
    counts.plot(kind="bar")
    plt.xlabel("Day of Week")
    plt.ylabel("Email Count")
    plt.title("Rejections by Day")
    plt.tight_layout()
    day_path = f"{prefix}_days.png"
    plt.savefig(day_path)

    plt.figure(figsize=(6, 4))
    df["Hour"].plot.hist(bins=24, range=(0, 23), edgecolor="black")
    plt.xlabel("Hour of Day")
    plt.ylabel("Email Count")
    plt.title("Rejections by Hour")
    plt.tight_layout()
    hour_path = f"{prefix}_hours.png"
    plt.savefig(hour_path)
    print(f"Saved {day_path} and {hour_path}")


def main(args: argparse.Namespace) -> None:
    df = load_data(args.csv)
    plot_timings(df, args.output_prefix)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Visualize timing of rejection emails")
    parser.add_argument("--csv", default="data/raw/rejections.csv", help="Path to CSV dataset")
    parser.add_argument("--output-prefix", default="rejection_timing", help="Prefix for output images")
    main(parser.parse_args())
