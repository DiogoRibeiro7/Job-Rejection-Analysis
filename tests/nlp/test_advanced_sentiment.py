import pandas as pd

from src.nlp.advanced_sentiment import transformer_sentiment


def test_transformer_sentiment_returns_labels():
    texts = pd.Series(["I love this job offer!", "This is a terrible rejection."])
    results = transformer_sentiment(
        texts, model_name="distilbert-base-uncased-finetuned-sst-2-english"
    )
    assert len(results) == 2
    assert all("label" in r and "score" in r for r in results)
