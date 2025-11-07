"""Visualize text clusters using t-SNE."""

import argparse
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.manifold import TSNE

from nlp_showcase import load_data


def plot_tsne(texts, n_clusters: int, output: str) -> None:
    """Cluster texts and plot t-SNE scatter."""
    vectorizer = TfidfVectorizer(stop_words="english", min_df=2)
    X = vectorizer.fit_transform(texts)
    km = KMeans(n_clusters=n_clusters, random_state=0, n_init=10)
    labels = km.fit_predict(X)
    tsne = TSNE(n_components=2, random_state=0, init="random", learning_rate="auto")
    reduced = tsne.fit_transform(X.toarray())
    plt.figure(figsize=(8, 6))
    plt.scatter(reduced[:, 0], reduced[:, 1], c=labels, cmap="tab10", alpha=0.7)
    plt.xlabel("t-SNE 1")
    plt.ylabel("t-SNE 2")
    plt.title("t-SNE Visualization of Email Clusters")
    plt.tight_layout()
    plt.savefig(output)
    print(f"Cluster plot saved to {output}")


def main(args: argparse.Namespace) -> None:
    df = load_data(args.csv)
    plot_tsne(df["full_text"], args.clusters, args.output)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Plot t-SNE clusters of rejection emails")
    parser.add_argument("--csv", default="data/rejections.csv", help="Path to CSV dataset")
    parser.add_argument("--clusters", type=int, default=3, help="Number of clusters")
    parser.add_argument("--output", default="clusters_tsne.png", help="Output image file")
    main(parser.parse_args())
