"""Visualize sentiment distribution of rejection emails."""

import argparse
import matplotlib.pyplot as plt

from nlp_showcase import load_data, sentiment_scores


def plot_histogram(texts, bins: int, output: str) -> None:
    """Plot histogram of sentiment scores and save the image."""
    scores = sentiment_scores(texts)
    plt.figure(figsize=(8, 4))
    plt.hist(scores, bins=bins, edgecolor="black")
    plt.xlabel("Sentiment score")
    plt.ylabel("Frequency")
    plt.title("Sentiment Distribution of Rejection Emails")
    plt.tight_layout()
    plt.savefig(output)
    print(f"Histogram saved to {output}")


def main(args: argparse.Namespace) -> None:
    df = load_data(args.csv)
    plot_histogram(df["full_text"], args.bins, args.output)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Plot sentiment distribution of rejection emails"
    )
    parser.add_argument(
        "--csv", default="data/rejections.csv", help="Path to CSV dataset"
    )
    parser.add_argument(
        "--bins", type=int, default=20, help="Number of histogram bins"
    )
    parser.add_argument(
        "--output", default="sentiment_histogram.png", help="Output image filename"
    )
    main(parser.parse_args())
