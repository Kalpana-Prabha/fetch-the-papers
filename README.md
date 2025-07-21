
# PubMed Fetcher

## Overview
Command-line tool that fetches PubMed research papers and filters for authors affiliated with pharmaceutical or biotech companies.

## Features
- Uses PubMed E-utilities API
- Filters based on simple heuristics
- Outputs to CSV or console
- Debug mode for verbose logging

## Setup

```bash
poetry install
```

## Usage

```bash
poetry run get-papers-list "cancer immunotherapy" -f results.csv
```

### Options
- `-f, --file` : Save results to CSV
- `-d, --debug`: Print debug logs

## Tools Used
- [NCBI PubMed API](https://www.ncbi.nlm.nih.gov/books/NBK25501/)
- [Poetry](https://python-poetry.org/)
- [Requests](https://requests.readthedocs.io/)

## Publishing to Test PyPI

```bash
poetry build
poetry publish -r testpypi
```
