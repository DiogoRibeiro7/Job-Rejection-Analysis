"""Topic modeling using Latent Semantic Analysis (LSA)."""

import argparse
import pandas as pd
from sklearn.decomposition import TruncatedSVD
from sklearn.feature_extraction.text import TfidfVectorizer

from .nlp_utils import DATA_PATH, load_data


def lsa_topics(texts: pd.Series, n_topics: int = 3, n_words: int = 5) -> list[list[str]]:
    """Return top terms for each LSA topic."""
    vectorizer = TfidfVectorizer(stop_words="english")
    X = vectorizer.fit_transform(texts)
    svd = TruncatedSVD(n_components=n_topics, random_state=0)
    svd.fit(X)
    terms = vectorizer.get_feature_names_out()
    topics: list[list[str]] = []
    for comp in svd.components_:
        top_idx = comp.argsort()[:-n_words - 1 : -1]
        topics.append([terms[i] for i in top_idx])
    return topics


def main(args: argparse.Namespace) -> None:
    df = load_data(args.csv)
    topics = lsa_topics(df["full_text"], args.topics, args.top_words)
    for idx, words in enumerate(topics):
        print(f"Topic {idx}: {', '.join(words)}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="LSA topic modeling of rejection emails"
    )
    parser.add_argument(
        "--csv",
        default=DATA_PATH,
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
