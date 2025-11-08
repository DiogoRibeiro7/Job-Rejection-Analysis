import pandas as pd
import pytest

from src.nlp import (
    load_data,
    sentiment_scores,
    common_words,
    cluster_texts,
)


def test_load_data_combines_subject_and_text(tmp_path):
    csv_file = tmp_path / "sample.csv"
    pd.DataFrame({"Subject": ["Hello"], "Text": ["World"]}).to_csv(
        csv_file, index=False
    )

    df = load_data(csv_file)
    assert df.loc[0, "full_text"] == "hello world"


def test_load_data_missing_columns(tmp_path):
    csv_file = tmp_path / "missing.csv"
    pd.DataFrame({"Subject": ["Hi"]}).to_csv(csv_file, index=False)

    with pytest.raises(ValueError):
        load_data(csv_file)


def test_sentiment_scores_distinguish_polarity():
    texts = pd.Series(["I love this", "I hate this"])
    scores = sentiment_scores(texts)
    assert len(scores) == 2
    assert scores[0] > scores[1]


def test_common_words_excludes_stopwords():
    texts = pd.Series(["this is a test this test is fun"])
    words = dict(common_words(texts, n=2))
    assert words == {"test": 2, "fun": 1}


def test_cluster_texts_shapes():
    texts = pd.Series(
        [
            "apple apple banana",
            "apple banana",
            "banana banana apple",
            "carrot carrot banana",
            "carrot banana banana",
            "carrot apple carrot",
        ]
    )
    labels, clusters = cluster_texts(texts, n_clusters=2, top_terms=2)
    assert len(labels) == len(texts)
    assert set(clusters.keys()) == {0, 1}
    assert all(len(t) == 2 for t in clusters.values())

