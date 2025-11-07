"""Utility functions for analyzing job rejection emails."""

from pathlib import Path

import pandas as pd
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk import FreqDist, wordpunct_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

nltk.download("punkt", quiet=True)
nltk.download("punkt_tab", quiet=True)
nltk.download("stopwords", quiet=True)
nltk.download("vader_lexicon", quiet=True)

DATA_PATH = Path(__file__).resolve().parent / "data" / "rejections.csv"


def load_data(csv_path: Path = DATA_PATH) -> pd.DataFrame:
    """Load dataset and combine subject and email text.

    Parameters
    ----------
    csv_path:
        Location of the CSV file. Defaults to ``DATA_PATH``.

    Returns
    -------
    pandas.DataFrame
        The loaded data with an additional ``full_text`` column.

    Raises
    ------
    FileNotFoundError
        If ``csv_path`` does not exist.
    ValueError
        If the required ``Subject`` or ``Text`` columns are missing.
    """

    csv_path = Path(csv_path)
    if not csv_path.exists():
        raise FileNotFoundError(f"CSV file not found: {csv_path}")

    df = pd.read_csv(csv_path)

    required_columns = {"Subject", "Text"}
    missing = required_columns.difference(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {', '.join(sorted(missing))}")

    df["full_text"] = (
        df["Subject"].fillna("") + " " + df["Text"].fillna("")
    ).str.lower()
    return df


def sentiment_scores(texts: pd.Series) -> list[float]:
    """Compute VADER sentiment scores for each text."""
    sia = SentimentIntensityAnalyzer()
    return [sia.polarity_scores(t)["compound"] for t in texts]


def common_words(texts: pd.Series, n: int = 20) -> list[tuple[str, int]]:
    """Return the most common non-stopword tokens."""
    stop_words = set(stopwords.words("english"))
    tokens: list[str] = []
    for text in texts:
        for word in wordpunct_tokenize(text):
            if word.isalpha() and word not in stop_words:
                tokens.append(word)
    freq = FreqDist(tokens)
    return freq.most_common(n)


def cluster_texts(
    texts: pd.Series, n_clusters: int = 3, top_terms: int = 5
) -> tuple[list[int], dict[int, list[str]]]:
    """Cluster texts using TF-IDF and K-means."""
    vectorizer = TfidfVectorizer(stop_words="english", min_df=2)
    X = vectorizer.fit_transform(texts)
    km = KMeans(n_clusters=n_clusters, random_state=0, n_init=10)
    labels = km.fit_predict(X)
    terms = vectorizer.get_feature_names_out()
    order_centroids = km.cluster_centers_.argsort()[:, ::-1]
    clusters = {
        i: [terms[ind] for ind in order_centroids[i, :top_terms]]
        for i in range(n_clusters)
    }
    return labels.tolist(), clusters

