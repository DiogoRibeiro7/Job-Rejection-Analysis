"""Plot top bigrams from rejection emails."""

import argparse
from collections import Counter

import matplotlib.pyplot as plt
from nltk import word_tokenize
from nltk.corpus import stopwords

from nlp_showcase import load_data


def top_bigrams(texts, top: int) -> list[tuple[tuple[str, str], int]]:
    """Return the most common bigrams excluding stopwords."""
    stop_words = set(stopwords.words("english"))
    counts: Counter[tuple[str, str]] = Counter()
    for text in texts:
        tokens = [w.lower() for w in word_tokenize(text) if w.isalpha() and w.lower() not in stop_words]
        for w1, w2 in zip(tokens, tokens[1:]):
            counts[(w1, w2)] += 1
    return counts.most_common(top)


def plot_bigrams(bigrams: list[tuple[tuple[str, str], int]], output: str) -> None:
    """Plot a horizontal bar chart of bigram frequencies."""
    labels = [f"{w1} {w2}" for (w1, w2), _ in bigrams]
    counts = [count for _, count in bigrams]
    plt.figure(figsize=(8, 4))
    plt.barh(labels[::-1], counts[::-1])
    plt.xlabel("Frequency")
    plt.title("Top Bigrams in Rejection Emails")
    plt.tight_layout()
    plt.savefig(output)
    print(f"Bigram chart saved to {output}")


def main(args: argparse.Namespace) -> None:
    df = load_data(args.csv)
    bigrams = top_bigrams(df["full_text"], args.top)
    plot_bigrams(bigrams, args.output)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Plot common bigrams from emails")
    parser.add_argument("--csv", default="data/rejections.csv", help="Path to CSV dataset")
    parser.add_argument("--top", type=int, default=10, help="Number of bigrams to plot")
    parser.add_argument("--output", default="bigrams.png", help="Output image file")
    main(parser.parse_args())
