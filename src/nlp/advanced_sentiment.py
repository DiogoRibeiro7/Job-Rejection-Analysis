"""Transformer-based sentiment analysis for rejection emails."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import List, Dict

import pandas as pd
from transformers import pipeline

from .nlp_utils import load_data


def transformer_sentiment(texts: pd.Series, model_name: str) -> List[Dict[str, float]]:
    """Compute sentiment using a transformer model.

    Parameters
    ----------
    texts:
        Series of text strings to analyze.
    model_name:
        Name of the Hugging Face model to use.
    """
    classifier = pipeline("sentiment-analysis", model=model_name)
    return classifier(texts.tolist())


def analyze_dataframe(df: pd.DataFrame, model_name: str) -> pd.DataFrame:
    """Apply transformer sentiment analysis to a DataFrame."""
    results = transformer_sentiment(df["full_text"], model_name)
    df = df.copy()
    df["sentiment_label"] = [r["label"] for r in results]
    df["sentiment_score"] = [r["score"] for r in results]
    return df


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Run transformer-based sentiment analysis on rejection emails"
    )
    parser.add_argument(
        "--csv",
        type=Path,
        default=None,
        help="Path to the rejection CSV file (defaults to data/raw/rejections.csv)",
    )
    parser.add_argument(
        "--model",
        type=str,
        default="distilbert-base-uncased-finetuned-sst-2-english",
        help="Hugging Face model name",
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="Optional path to save the annotated CSV",
    )
    args = parser.parse_args()

    df = load_data(args.csv) if args.csv else load_data()
    df = analyze_dataframe(df, args.model)

    if args.output:
        df.to_csv(args.output, index=False)
        print(f"Saved results to {args.output}")
    else:
        print(df[["Subject", "sentiment_label", "sentiment_score"]].head().to_string(index=False))


if __name__ == "__main__":
    main()
