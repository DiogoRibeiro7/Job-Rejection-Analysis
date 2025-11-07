"""Utilities for collecting public job rejection templates."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, List
import csv
import requests
from bs4 import BeautifulSoup


@dataclass
class Template:
    """Represents a collected template."""
    source: str
    text: str
    error: str = ""


def fetch_template(url: str) -> str:
    """Fetch and return visible text from a URL.

    Parameters
    ----------
    url: str
        The URL to download.

    Returns
    -------
    str
        Extracted plain text from the page.
    """
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    return soup.get_text(" ", strip=True)


def collect_templates(urls: Iterable[str], output_csv: str) -> List[Template]:
    """Collect templates from a list of URLs and write them to a CSV file.

    Errors are captured per URL rather than aborting the entire process.

    Parameters
    ----------
    urls: Iterable[str]
        URLs to attempt to download.
    output_csv: str
        Destination CSV path.

    Returns
    -------
    List[Template]
        The collected templates.
    """
    results: List[Template] = []
    for url in urls:
        try:
            text = fetch_template(url)
            results.append(Template(source=url, text=text))
        except Exception as exc:  # pragma: no cover - network failure path
            results.append(Template(source=url, text="", error=str(exc)))
    with open(output_csv, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["source", "text", "error"])
        writer.writeheader()
        for tmpl in results:
            writer.writerow({"source": tmpl.source, "text": tmpl.text, "error": tmpl.error})
    return results


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Collect public job rejection templates")
    parser.add_argument("urls", nargs="*", help="Template URLs to download")
    parser.add_argument("--output", default="data/templates.csv", help="Output CSV path")
    args = parser.parse_args()

    collect_templates(args.urls, args.output)
