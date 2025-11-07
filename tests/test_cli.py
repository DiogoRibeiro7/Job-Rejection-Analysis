import subprocess
import sys


def write_sample_csv(path):
    path.write_text("Subject,Text\nhi,Thanks but no thanks\nhello,We selected others")


def test_sentiment_cli(tmp_path):
    csv = tmp_path / "s.csv"
    write_sample_csv(csv)
    result = subprocess.run(
        [sys.executable, "nlp_cli.py", "sentiment", "--csv", str(csv)],
        capture_output=True,
        text=True,
        check=True,
    )
    assert "Average sentiment" in result.stdout
