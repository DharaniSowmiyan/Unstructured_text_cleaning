import re
from bs4 import BeautifulSoup, Comment
from langdetect import detect, LangDetectException
from typing import List, Optional

# Import the noise patterns from your constants file
from constants import NOISE_PATTERNS

# --- Recursive Character Splitting Function remains the same ---
def recursive_character_split(text: str, chunk_size: int = 1000, chunk_overlap: int = 150) -> List[str]:
    """
    Splits text recursively into chunks of a specified size with overlap.
    This method tries to split on natural boundaries like paragraphs and sentences first.
    """
    if not text or len(text) <= chunk_size:
        return [text] if text else []

    separators = ["\n\n", "\n", ". ", " ", ""]
    effective_separator = ""
    for sep in separators:
        if sep in text:
            effective_separator = sep
            break
            
    splits = text.split(effective_separator)
    
    chunks = []
    current_chunk = ""
    for s in splits:
        if len(current_chunk) + len(s) + len(effective_separator) <= chunk_size:
            current_chunk += s + effective_separator
        else:
            if current_chunk:
                chunks.append(current_chunk.strip())
            current_chunk = s + effective_separator
    
    if current_chunk:
        chunks.append(current_chunk.strip())
        
    final_chunks = []
    for chunk in chunks:
        if len(chunk) > chunk_size:
            final_chunks.extend(recursive_character_split(chunk, chunk_size, chunk_overlap))
        else:
            final_chunks.append(chunk)

    return [chunk for chunk in final_chunks if chunk.strip()]


# --- Helper functions remain the same ---
def _extract_main_content(soup: BeautifulSoup) -> Optional[BeautifulSoup]:
    """Finds and returns the main content block from a parsed HTML soup."""
    main_content_selectors = ['main', 'article', '[role="main"]', '#content', '#main']
    for selector in main_content_selectors:
        found_content = soup.select_one(selector)
        if found_content:
            return found_content
    return soup.body if soup.body else soup

def _remove_unwanted_elements(soup: BeautifulSoup) -> None:
    """Removes comments and unwanted tags from the soup object in-place."""
    for comment in soup.find_all(string=lambda text: isinstance(text, Comment)):
        comment.extract()
    tags_to_remove = ['script', 'style', 'nav', 'footer', 'header', 'aside', 'form']
    for tag in soup(tags_to_remove):
        tag.decompose()

def _filter_and_clean_chunks(potential_chunks: List[str]) -> List[str]:
    """Cleans, normalizes, and filters text chunks for English content."""
    cleaned_chunks = []
    noise_regex = re.compile('|'.join(re.escape(p) for p in NOISE_PATTERNS), re.IGNORECASE)
    for text in potential_chunks:
        text = text.strip()
        text = noise_regex.sub('', text)
        text = re.sub(r'[^a-z0-9\s.?!]', '', text, flags=re.IGNORECASE)
        text = re.sub(r'\s+', ' ', text).strip().lower()
        if text and len(text.split()) >= 4:
            try:
                if detect(text) == 'en':
                    cleaned_chunks.append(text)
            except LangDetectException:
                continue
    return cleaned_chunks

def _deduplicate_chunks(chunks: List[str]) -> List[str]:
    """Removes duplicate strings from a list while preserving order."""
    return list(dict.fromkeys(chunks))


# --- NEW: Unified function to handle both HTML and Plain Text ---
def clean_content(raw_content: str) -> List[str]:
    """
    Orchestrates the cleaning of raw content, automatically detecting if it's HTML.
    """
    if not raw_content:
        return []

    full_text = ""
    # Check for basic HTML tags to decide which pipeline to use
    if '<html' in raw_content.lower() or '<body' in raw_content.lower() or '<div' in raw_content.lower():
        print("🔬 Using HTML cleaning pipeline...")
        soup = BeautifulSoup(raw_content, 'lxml')
        main_soup = _extract_main_content(soup)
        if main_soup:
            _remove_unwanted_elements(main_soup)
            full_text = main_soup.get_text(separator='\n\n', strip=True)
        else:
            full_text = raw_content # Fallback if parsing fails
    else:
        print("🔬 Using Plain Text cleaning pipeline...")
        full_text = raw_content

    potential_chunks = recursive_character_split(full_text)
    english_chunks = _filter_and_clean_chunks(potential_chunks)
    return _deduplicate_chunks(english_chunks)
