from pubmed_fetcher.fetch import fetch_pubmed_ids, fetch_paper_details
from pubmed_fetcher.filter import is_non_academic
from pubmed_fetcher.utils import extract_email
from typing import List, Dict

def get_filtered_papers(query: str, debug: bool = False) -> List[Dict]:
    ids = fetch_pubmed_ids(query)
    results = []

    for pid in ids:
        detail = fetch_paper_details(pid)
        # parse XML and extract info: title, authors, affiliations
        # filter non-academic authors
        # collect corresponding email
        # append dict to results
        pass  # you'll fill in this logic using xml.etree.ElementTree

    return results
