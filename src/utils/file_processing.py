from pathlib import Path
import io
import logging
import tiktoken
import docx
import markdown
import re

from utils.document_helpers import parse_raw_document, format_filename, check_token_count
from utils.llm import llm, prompts
from config import HEADER, DISCLAIMER


def process_file(raw_file: Path, output_path: Path) -> bool:
    """
    Process the raw file to generate a cleaned and formatted transcript.

    Args:
        raw_file (Path): The path to the raw input file.
        output_path (Path): The path to the directory where the output file will be saved.

    Returns:
        bool: True if processing was successful, False otherwise.
    """
    try:
        logging.info(f"Processing file: {raw_file}")
        
        # Parse raw file
        raw_text = parse_raw_document(raw_file)

        # Check token count of raw text
        if not check_token_count(raw_text):
            logging.error(f"Text from {raw_file} exceeds maximum token limit, consider chunking")
            return False

        # Obtain final doc
        processed_text = llm(
            system_prompt=prompts["USER_GUIDE"],
            user_text=raw_text,
        )

        # Add header and disclaimer
        final_text = HEADER + processed_text + DISCLAIMER
        
        # Save output
        output_file = output_path / f"{format_filename(raw_file.stem)}___ai_processed_transcript.html"
        output_file.write_text(markdown.markdown(final_text), encoding='utf-8')
        
        logging.info(f"Successfully processed {raw_file} -> {output_file}")
        return True
        
    except Exception as e:
        logging.error(f"Error processing {raw_file}: {str(e)}")
        return False
