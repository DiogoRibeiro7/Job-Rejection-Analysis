"""Simple topic modeling using LDA on the rejection emails."""

import argparse

import pandas as pd
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

nltk.download("punkt", quiet=True)
nltk.download("punkt_tab", quiet=True)


def load_texts(csv_path: str = "data/rejections.csv") -> pd.Series:
    """Return lowercase full text from the dataset."""
    df = pd.read_csv(csv_path)
    texts = (df["Subject"].fillna("") + " " + df["Text"].fillna(""))
    return texts.str.lower()


def lda_topics(texts: pd.Series, n_topics: int = 3, n_words: int = 5) -> None:
    """Print top terms for each LDA topic."""
    vectorizer = CountVectorizer(
        stop_words="english",
        token_pattern=r"(?u)\b\w+\b",
        min_df=1,
    )
    X = vectorizer.fit_transform(texts)
    lda = LatentDirichletAllocation(n_components=n_topics, random_state=0)
    lda.fit(X)
    terms = vectorizer.get_feature_names_out()
    for idx, topic in enumerate(lda.components_):
        top_indices = topic.argsort()[:-n_words - 1:-1]
        words = ", ".join(terms[i] for i in top_indices)
        print(f"Topic {idx}: {words}")


def main(args: argparse.Namespace) -> None:
    texts = load_texts(args.csv)
    lda_topics(texts, args.topics, args.top_words)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="LDA topic modeling of rejection emails"
    )
    parser.add_argument(
        "--csv",
        default="data/rejections.csv",
        help="Path to CSV dataset",
    )
    parser.add_argument(
        "--topics",
        type=int,
        default=3,
        help="Number of topics",
    )
    parser.add_argument(
        "--top-words",
        type=int,
        default=5,
        help="Words to show per topic",
    )
    main(parser.parse_args())
