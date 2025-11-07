"""Compute readability statistics for rejection emails."""

import argparse
from typing import Tuple

from textstat import textstat

from nlp_showcase import load_data


def compute_metrics(texts) -> Tuple[list[float], list[float]]:
    """Return Flesch Reading Ease and Flesch-Kincaid grade for each text."""
    ease_scores = [textstat.flesch_reading_ease(t) for t in texts]
    grade_scores = [textstat.flesch_kincaid_grade(t) for t in texts]
    return ease_scores, grade_scores


def main(args: argparse.Namespace) -> None:
    df = load_data(args.csv)
    ease, grade = compute_metrics(df["full_text"])
    avg_ease = sum(ease) / len(ease)
    avg_grade = sum(grade) / len(grade)
    print(f"Average Flesch Reading Ease: {avg_ease:.2f}")
    print(f"Average Flesch-Kincaid Grade: {avg_grade:.2f}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Compute readability metrics")
    parser.add_argument("--csv", default="data/rejections.csv", help="Path to CSV data")
    main(parser.parse_args())
