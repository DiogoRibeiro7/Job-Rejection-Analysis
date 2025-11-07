import pandas as pd

from topic_modeling_lsa import lsa_topics


def test_lsa_topics_shape():
    texts = pd.Series(
        [
            "data science rejection notice",
            "software engineer application denied",
            "we chose other candidates",
        ]
    )
    topics = lsa_topics(texts, n_topics=2, n_words=3)
    assert len(topics) == 2
    assert all(len(t) == 3 for t in topics)
