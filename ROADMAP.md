# Roadmap

This document outlines planned improvements and future directions for the Job-Rejection-Analysis project.

## Short-term
 - [x] Expand the dataset with additional rejection emails to improve statistical reliability.
- [x] Refine `nlp_showcase.py` by separating concerns into reusable utility modules.
- [x] Add continuous integration to automatically run tests on each commit.
- [x] Provide example scripts for visualizing trends across time and companies.

## Medium-term
- [x] Explore advanced topic modeling techniques (e.g., BERTopic, LSA) for deeper insight.
- [x] Build a small web dashboard to interactively explore the dataset.
- [x] Implement a CLI for common tasks like data cleaning, sentiment analysis, and clustering.
- [x] Integrate transformer-based sentiment analysis for more nuanced emotion detection.

## Long-term
 - [x] Develop a pipeline for automated collection of public job rejection templates.
- [ ] Publish an accompanying article or blog post summarizing key findings.
- [ ] Package the project for distribution on PyPI once APIs and interfaces stabilize.

## Enterprise expansion
- [x] Introduce basic tenant management for multi-tenant data separation.
- [ ] Implement role-based access control for different user types.

## Open Data Standard
- [x] Publish a JSON schema and sample dataset for job market records.
- [x] Provide a data validation library for enforcing the schema.
- [x] Support basic schema versioning.
- [ ] Provide multi-language reference implementations and privacy guidelines.

Suggestions and contributions are welcome. Please open an issue or pull request to discuss ideas.
