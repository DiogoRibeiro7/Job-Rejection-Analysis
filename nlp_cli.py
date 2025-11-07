"""Command-line interface for common NLP tasks."""

import argparse
from typing import Callable

from nlp_utils import (
    DATA_PATH,
    cluster_texts,
    common_words,
    load_data,
    sentiment_scores,
)


def cmd_sentiment(args: argparse.Namespace) -> None:
    df = load_data(args.csv)
    scores = sentiment_scores(df["full_text"])
    avg = sum(scores) / len(scores)
    print(f"Average sentiment: {avg:.3f}")


def cmd_top_words(args: argparse.Namespace) -> None:
    df = load_data(args.csv)
    words = common_words(df["full_text"], args.top)
    for word, freq in words:
        print(f"{word}: {freq}")


def cmd_cluster(args: argparse.Namespace) -> None:
    df = load_data(args.csv)
    _, clusters = cluster_texts(
        df["full_text"], args.clusters, args.top_terms
    )
    for idx, terms in clusters.items():
        print(f"Cluster {idx}: {', '.join(terms)}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="NLP helper CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    sent = subparsers.add_parser(
        "sentiment", help="Compute average sentiment score"
    )
    sent.add_argument("--csv", default=DATA_PATH, help="Path to CSV dataset")
    sent.set_defaults(func=cmd_sentiment)

    top = subparsers.add_parser(
        "top-words", help="List most frequent words"
    )
    top.add_argument("--csv", default=DATA_PATH, help="Path to CSV dataset")
    top.add_argument("--top", type=int, default=10, help="Number of words")
    top.set_defaults(func=cmd_top_words)

    cluster = subparsers.add_parser(
        "cluster", help="Cluster texts and show top terms"
    )
    cluster.add_argument("--csv", default=DATA_PATH, help="Path to CSV dataset")
    cluster.add_argument("--clusters", type=int, default=3)
    cluster.add_argument("--top-terms", type=int, default=5)
    cluster.set_defaults(func=cmd_cluster)

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    func: Callable[[argparse.Namespace], None] = args.func
    func(args)


if __name__ == "__main__":
    main()
