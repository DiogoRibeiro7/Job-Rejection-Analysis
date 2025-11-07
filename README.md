# Job-Rejection-Analysis
Exploratory data analysis of job rejection emails

### Introduction
Nobody likes getting that rejection email after applying for a job, but it happens. The question remains: what do we do when it happens? I scraped over 80 job rejections from my inbox and continue to expand the dataset for stronger statistics. I dive into questions regarding the time and day the email was sent as well as the content of the email itself.

### Repository Structure
- `data/rejections.csv` contains the collected rejection emails.
- `notebooks/` holds Jupyter notebooks for data collection and exploratory analysis.
- Python scripts in the project root perform command-line analyses and visualizations.
- `web_dashboard.py` offers an interactive Streamlit dashboard for exploring the data.
- `nlp_utils.py` contains reusable NLP helper functions.
- See `ROADMAP.md` for planned enhancements and future directions.
- `tenant_management/` houses early building blocks for enterprise multi-tenant features.
- `email_scraper/` provides a simple pipeline for gathering public rejection templates.
### Open Data Standard and API
- `schemas/v1/job_market_data.schema.json` defines the **v1** JSON schema for job‑market records.
- `schema_versioning/` helps retrieve specific schema versions.
- `validation/` offers helpers to validate data against the schema.
- `data/rejection_schema_example.json` provides a sample conforming to the schema.
- `api/main.py` exposes a minimal FastAPI service; run `poetry run uvicorn api.main:app --reload` to start.


### NLP Showcase
The script `nlp_showcase.py` showcases basic NLP techniques on the dataset. It
computes sentiment scores with NLTK, reports frequent words (ignoring stop
words) and groups similar emails using TF‑IDF features and K‑means.
Command‑line arguments allow you to specify the input file, number of clusters
and how many common words to display.



`topic_modeling.py` extends the analysis by fitting an LDA model and printing the top terms for each topic. `topic_modeling_lsa.py` demonstrates Latent Semantic Analysis (LSA) for an alternative topic perspective. The script `visualize_sentiment.py` draws a
histogram of VADER sentiment scores so you can quickly gauge the overall tone of
the emails. `visualize_clusters.py` projects TF‑IDF features with t‑SNE so you
can see how the rejection emails group together visually. `extract_named_entities.py`
uses NLTK's built‑in chunker to list the most common names and organizations
mentioned in the rejection text.
`summarize_emails.py` condenses the dataset using a simple TF‑IDF
scoring approach, providing a quick overview of the typical rejection
message.
`visualize_timings.py` charts when rejections arrive by day of the week and
hour of the day, saving two bar plots for quick reference. `visualize_trends.py` compares monthly rejection counts and top companies. `visualize_lengths.py`
plots a histogram of word counts so you can see how long these emails tend to be.
`nlp_cli.py` wraps common analysis steps (sentiment, frequent words, clustering) into a single command-line tool.
`advanced_sentiment.py` leverages a transformer model for more accurate sentiment classification.
`visualize_bigrams.py` highlights the most common two-word phrases.
`readability_metrics.py` reports the average Flesch reading ease and grade level
of the rejection texts. `visualize_pos_tags.py` counts part-of-speech tags to
show the grammatical makeup of the emails. `web_dashboard.py` launches an
interactive Streamlit app for exploring trends.

Install dependencies with [Poetry](https://python-poetry.org/) and run the
analysis scripts (which expect `data/rejections.csv`) using `poetry run`:

```bash
poetry install
poetry run python nlp_showcase.py --clusters 3 --top-words 20
poetry run python topic_modeling.py --topics 3 --top-words 5
poetry run python topic_modeling_lsa.py --topics 3 --top-words 5
poetry run python visualize_sentiment.py --bins 15
poetry run python visualize_clusters.py --clusters 3 --output tsne.png
poetry run python extract_named_entities.py --top 5
poetry run python generate_wordcloud.py --max-words 200 --output wordcloud.png
poetry run python summarize_emails.py --words 150
poetry run python visualize_timings.py --output-prefix timing
poetry run python nlp_cli.py sentiment
poetry run python advanced_sentiment.py --csv data/rejections.csv
poetry run python visualize_trends.py
poetry run python visualize_lengths.py --bins 20 --output lengths.png
poetry run python visualize_bigrams.py --top 10 --output bigrams.png
poetry run python readability_metrics.py
poetry run python visualize_pos_tags.py --output pos_tags.png
poetry run streamlit run web_dashboard.py
poetry run uvicorn api.main:app --reload
poetry run python -m email_scraper https://example.com/template1 https://example.com/template2 --output data/templates.csv
poetry run python - <<'PY'
from tenant_management import TenantManager, Tenant
manager = TenantManager(); manager.add_tenant(Tenant('demo', 'Demo Corp'))
print(list(t.name for t in manager.list_tenants()))
PY
```
