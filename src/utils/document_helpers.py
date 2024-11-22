from pathlib import Path
import docx
import re
import tiktoken
from typing import List


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


def chunk_text(text: str, chunk_size: int = 6000, overlap: int = 0) -> List[str]:
    """
    Chunk the text into smaller segments based on token count.
    
    Args:
        text (str): The input text to be chunked.
        chunk_size (int, optional): The size of each chunk in tokens. Defaults to 6000.
        overlap (int, optional): The number of overlapping tokens between chunks. Defaults to 0.
        
    Returns:
        List[str]: A list of text chunks.
    """
    encoding = tiktoken.get_encoding("cl100k_base")
    tokens = encoding.encode(text)
    chunks = []
    
    i = 0
    while i < len(tokens):
        # Get chunk of tokens
        chunk_tokens = tokens[i:i + chunk_size]
        # Decode chunk back to text
        chunk_text = encoding.decode(chunk_tokens)
        chunks.append(chunk_text)
        # Move to next chunk, considering overlap
        i += (chunk_size - overlap)
    
    return chunks
