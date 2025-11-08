"""Utility script demonstrating NLP techniques on the rejection dataset."""

import argparse
from collections import Counter

from .nlp_utils import (
    DATA_PATH,
    load_data,
    sentiment_scores,
    common_words,
    cluster_texts,
)


def main(args: argparse.Namespace) -> None:
    """Run analysis and display simple textual summary."""
    df = load_data(args.csv)
    sentiments = sentiment_scores(df["full_text"])
    df["sentiment"] = sentiments

    print(f"Average sentiment score: {sum(sentiments) / len(sentiments):.4f}")
    print("\nMost common words:")
    for word, count in common_words(df["full_text"], args.top_words):
        print(f"{word}: {count}")

    labels, clusters = cluster_texts(df["full_text"], args.clusters)
    print("\nCluster sizes:", Counter(labels))
    for idx, terms in clusters.items():
        print(f"Cluster {idx} top terms: {', '.join(terms)}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Analyze rejection emails with simple NLP techniques",
    )
    parser.add_argument(
        "--csv",
        default=DATA_PATH,
        help="Path to CSV file containing the emails",
    )
    parser.add_argument(
        "--clusters", type=int, default=3, help="Number of clusters to compute"
    )
    parser.add_argument(
        "--top-words", type=int, default=20, help="Number of frequent words"
    )
    main(parser.parse_args())

