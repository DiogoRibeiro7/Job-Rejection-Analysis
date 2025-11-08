"""NLP module for analyzing job rejection emails."""

from .nlp_utils import (
    load_data,
    sentiment_scores,
    common_words,
    cluster_texts,
    DATA_PATH,
)
from .advanced_sentiment import (
    transformer_sentiment,
    analyze_dataframe,
)
from .summarize_emails import summarize_texts

__all__ = [
    # Core utilities
    "load_data",
    "sentiment_scores",
    "common_words",
    "cluster_texts",
    "DATA_PATH",
    # Advanced sentiment
    "transformer_sentiment",
    "analyze_dataframe",
    # Summarization
    "summarize_texts",
]
