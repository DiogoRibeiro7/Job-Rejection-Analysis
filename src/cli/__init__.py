"""Command-line interface module for job rejection analysis."""

from .main import (
    build_parser,
    main,
    cmd_sentiment,
    cmd_top_words,
    cmd_cluster,
)

__all__ = [
    "build_parser",
    "main",
    "cmd_sentiment",
    "cmd_top_words",
    "cmd_cluster",
]
