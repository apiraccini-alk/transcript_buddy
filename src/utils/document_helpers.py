from pathlib import Path
import docx
import re
import tiktoken
from typing import List

from config import MAX_TOKENS


def format_filename(filename: str) -> str:
    """
    Format the filename by removing special characters and spaces.
    
    Args:
        filename (str): The input filename to format.
        
    Returns:
        str: The formatted filename.
    """
    # Remove special characters and replace spaces with underscores
    formatted = re.sub(r'[^\w\s-]', '', filename)
    return formatted.strip().replace(' ', '_')


def parse_raw_document(raw_file: Path) -> str:
    """
    Parse the raw document to extract text.
    
    Args:
        raw_file (Path): The path to the raw input file.
        
    Returns:
        str: The extracted text from the document.
    """
    doc = docx.Document(raw_file)
    paragraphs = [p.text.strip() for p in doc.paragraphs if p.text.strip()]
    return '\n'.join(paragraphs)


def check_token_count(text: str, max_tokens: int = MAX_TOKENS) -> bool:
    """
    Check if the text exceeds the maximum token limit.
    
    Args:
        text (str): The text to check
        max_tokens (int): Maximum number of tokens allowed
        
    Returns:
        bool: True if within limit, False if exceeds
    """
    encoding = tiktoken.get_encoding("cl100k_base")
    num_tokens = len(encoding.encode(text))
    return num_tokens <= max_tokens
