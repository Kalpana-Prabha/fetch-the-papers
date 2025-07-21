def is_non_academic(affil: str) -> bool:
    academic_terms = ["university", "college", "institute", "hospital"]
    non_academic_terms = ["pharma", "biotech", "inc", "ltd", "corporation", "gmbh"]

    affil_lower = affil.lower()
    return any(term in affil_lower for term in non_academic_terms) and \
           not any(term in affil_lower for term in academic_terms)
