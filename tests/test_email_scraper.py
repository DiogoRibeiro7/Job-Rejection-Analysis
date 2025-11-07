import csv
from pathlib import Path
from unittest.mock import patch, Mock

from email_scraper import collect_templates


def test_collect_templates(tmp_path: Path):
    html = "<html><body><p>Example rejection template</p></body></html>"

    def fake_get(url, timeout=10):
        mock = Mock()
        mock.text = html
        mock.raise_for_status = lambda: None
        return mock

    output = tmp_path / "templates.csv"
    with patch("requests.get", fake_get):
        results = collect_templates(["http://example.com/template"], str(output))

    assert output.exists()
    with output.open() as f:
        rows = list(csv.DictReader(f))
    assert rows[0]["source"] == "http://example.com/template"
    assert "Example rejection template" in rows[0]["text"]
    assert results[0].text.startswith("Example rejection template")
