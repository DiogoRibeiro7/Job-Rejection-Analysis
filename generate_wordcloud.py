"""Generate a word cloud of common words in the rejection emails."""

import argparse
from wordcloud import WordCloud, STOPWORDS

from nlp_showcase import load_data


def create_wordcloud(texts, max_words: int, output: str) -> None:
    """Generate and save a word cloud image."""
    text = " ".join(texts)
    wc = WordCloud(
        width=800,
        height=400,
        background_color="white",
        stopwords=STOPWORDS,
        max_words=max_words,
    )
    wc.generate(text)
    wc.to_file(output)
    print(f"Word cloud saved to {output}")


def main(args: argparse.Namespace) -> None:
    df = load_data(args.csv)
    create_wordcloud(df["full_text"], args.max_words, args.output)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a word cloud from emails")
    parser.add_argument("--csv", default="data/rejections.csv", help="Path to CSV dataset")
    parser.add_argument("--max-words", type=int, default=200, help="Maximum words in the cloud")
    parser.add_argument("--output", default="wordcloud.png", help="Output image file")
    main(parser.parse_args())
