from typing import List, Dict
import requests
import xml.etree.ElementTree as ET

def fetch_pubmed_ids(query: str, retmax: int = 100) -> List[str]:
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {
        "db": "pubmed",
        "term": query,
        "retmode": "xml",
        "retmax": retmax
    }
    response = requests.get(url, params=params)
    root = ET.fromstring(response.text)
    return [id_elem.text for id_elem in root.findall(".//Id")]

def fetch_paper_details(pubmed_id: str) -> Dict:
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
    params = {
        "db": "pubmed",
        "id": pubmed_id,
        "retmode": "xml"
    }
    response = requests.get(url, params=params)
    return {"xml": response.text, "pubmed_id": pubmed_id}
