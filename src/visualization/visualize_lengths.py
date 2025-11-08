"""Plot histogram of rejection email lengths in words."""

import argparse
import matplotlib.pyplot as plt

from nlp import load_data


def plot_lengths(texts, bins: int, output: str) -> None:
    """Plot histogram of word counts and save image."""
    lengths = [len(t.split()) for t in texts]
    plt.figure(figsize=(8, 4))
    plt.hist(lengths, bins=bins, edgecolor="black")
    plt.xlabel("Word Count")
    plt.ylabel("Frequency")
    plt.title("Distribution of Email Lengths")
    plt.tight_layout()
    plt.savefig(output)
    print(f"Length histogram saved to {output}")


def main(args: argparse.Namespace) -> None:
    df = load_data(args.csv)
    plot_lengths(df["full_text"], args.bins, args.output)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Plot histogram of rejection email lengths"
    )
    parser.add_argument("--csv", default="data/raw/rejections.csv", help="Path to CSV dataset")
    parser.add_argument("--bins", type=int, default=20, help="Histogram bins")
    parser.add_argument(
        "--output", default="lengths_histogram.png", help="Output image file"
    )
    main(parser.parse_args())
