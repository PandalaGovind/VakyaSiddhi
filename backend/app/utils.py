import re

def clean_text(text: str) -> str:
    """Normalize text by converting to lowercase and stripping extra spaces."""
    return text.lower().strip()

def extract_words(text: str) -> list[str]:
    """Extract individual words from text using regex."""
    return re.findall(r'\w+', clean_text(text))