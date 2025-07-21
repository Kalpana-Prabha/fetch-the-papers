
import argparse
from pubmed_fetcher.main import get_filtered_papers
import csv

def main():
    parser = argparse.ArgumentParser(description="Fetch PubMed papers with biotech affiliations.")
    parser.add_argument("query", help="PubMed search query")
    parser.add_argument("-f", "--file", help="Output CSV file")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug output")

    args = parser.parse_args()
    results = get_filtered_papers(args.query, debug=args.debug)

    if not results:
        print("No results found.")
        return

    if args.file:
        with open(args.file, "w", newline='', encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=results[0].keys())
            writer.writeheader()
            writer.writerows(results)
    else:
        for row in results:
            print(row)
