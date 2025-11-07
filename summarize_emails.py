"""Summarize rejection emails using simple TF-IDF scoring."""

import argparse
from nltk import sent_tokenize
import nltk
import re
from sklearn.feature_extraction.text import TfidfVectorizer

from nlp_showcase import load_data

nltk.download("punkt", quiet=True)


def summarize_texts(texts, words: int) -> str:
    """Return a summary built from the highest scoring sentences."""
    combined = " ".join(texts)
    combined = re.sub(r"<[^>]+>", " ", combined)
    sentences = sent_tokenize(combined)
    if not sentences:
        return ""
    vectorizer = TfidfVectorizer(stop_words="english")
    X = vectorizer.fit_transform(sentences)
    scores = X.sum(axis=1).A1
    ranked = [sent for _, sent in sorted(zip(scores, sentences), reverse=True)]
    summary = []
    total_words = 0
    for sent in ranked:
        w = len(sent.split())
        if total_words + w > words:
            if not summary:
                summary.append(" ".join(sent.split()[: words - total_words]))
            break
        summary.append(sent)
        total_words += w
    return " ".join(summary)


def main(args: argparse.Namespace) -> None:
    df = load_data(args.csv)
    summary = summarize_texts(df["full_text"], args.words)
    print(summary)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Summarize rejection emails")
    parser.add_argument("--csv", default="data/rejections.csv", help="Path to CSV dataset")
    parser.add_argument("--words", type=int, default=100, help="Maximum words in summary")
    main(parser.parse_args())
