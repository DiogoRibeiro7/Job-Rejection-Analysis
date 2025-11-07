"""Extract named entities from rejection emails."""

import argparse
from collections import Counter, defaultdict

import pandas as pd
import nltk
from nltk import ne_chunk, pos_tag, word_tokenize
from nltk.tree import Tree

from nlp_showcase import load_data

# Download required NLTK models
nltk.download("punkt", quiet=True)
nltk.download("averaged_perceptron_tagger", quiet=True)
nltk.download("averaged_perceptron_tagger_eng", quiet=True)
nltk.download("maxent_ne_chunker", quiet=True)
nltk.download("maxent_ne_chunker_tab", quiet=True)
nltk.download("words", quiet=True)


def extract_entities(texts: pd.Series, top: int) -> dict[str, list[tuple[str, int]]]:
    """Return top named entities grouped by label."""
    counts: defaultdict[str, Counter] = defaultdict(Counter)
    for text in texts:
        tokens = word_tokenize(text)
        tagged = pos_tag(tokens)
        tree = ne_chunk(tagged)
        for subtree in tree:
            if isinstance(subtree, Tree):
                label = subtree.label()
                name = " ".join(word for word, _ in subtree.leaves())
                counts[label][name] += 1
    return {label: counter.most_common(top) for label, counter in counts.items()}


def main(args: argparse.Namespace) -> None:
    df = load_data(args.csv)
    entities = extract_entities(df["full_text"], args.top)
    for label, items in entities.items():
        print(f"\n{label}:")
        for name, count in items:
            print(f"  {name}: {count}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract named entities from emails")
    parser.add_argument("--csv", default="data/rejections.csv", help="Path to CSV dataset")
    parser.add_argument("--top", type=int, default=5, help="Number of entities per label")
    main(parser.parse_args())
