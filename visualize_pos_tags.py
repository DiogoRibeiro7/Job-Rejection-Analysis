"""Visualize distribution of part-of-speech tags in rejection emails."""

import argparse
from collections import Counter

import matplotlib.pyplot as plt
import nltk
from nltk import word_tokenize, pos_tag

from nlp_showcase import load_data

nltk.download("punkt", quiet=True)
nltk.download("averaged_perceptron_tagger", quiet=True)


def pos_distribution(texts):
    """Return counts of POS tags across all texts."""
    counts: Counter[str] = Counter()
    for text in texts:
        tokens = [w for w in word_tokenize(text) if w.isalpha()]
        tags = pos_tag(tokens)
        for _, tag in tags:
            counts[tag] += 1
    return counts


def plot_pos(counts: Counter[str], output: str) -> None:
    """Plot a bar chart of POS tag counts."""
    tags, values = zip(*counts.most_common())
    plt.figure(figsize=(10, 4))
    plt.bar(tags, values)
    plt.xlabel("POS Tag")
    plt.ylabel("Frequency")
    plt.title("Part-of-Speech Distribution")
    plt.tight_layout()
    plt.savefig(output)
    print(f"POS tag chart saved to {output}")


def main(args: argparse.Namespace) -> None:
    df = load_data(args.csv)
    counts = pos_distribution(df["full_text"])
    plot_pos(counts, args.output)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Visualize part-of-speech tag distribution"
    )
    parser.add_argument("--csv", default="data/rejections.csv", help="Path to CSV dataset")
    parser.add_argument(
        "--output", default="pos_tags.png", help="Output image file"
    )
    main(parser.parse_args())
