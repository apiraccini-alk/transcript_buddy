from pathlib import Path
import io
import logging
import tiktoken
import docx
import markdown
import re

from utils.document_helpers import parse_raw_document, chunk_text, format_filename
from utils.llm import llm, prompts


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
        
        # Obtain text chunks
        text_chunks = chunk_text(raw_text)
        
        # Clean text chunks
        cleaned_chunks = []
        for i, chunk in enumerate(text_chunks, 1):
            logging.info(f"Processing chunk {i}/{len(text_chunks)}")
            chunk_summary = llm(
                system_prompt=prompts["CLEANER"],
                user_text=f"This is the transcript chunk: {chunk}",
            )
            cleaned_chunks.append(chunk_summary)
        
        # Combine cleaned chunks and format
        cleaned_text = "\n\n".join(cleaned_chunks)
        
        # Add header and disclaimer
        header = "*Amplifon CoE - Alkemy - onboarding sessions*\n\n---\n\n"
        disclaimer = "\n\n---\n\n*This text was generated by an AI language model and may contain errors or inaccuracies.*"
        final_text = header + cleaned_text + disclaimer
        
        # Save output
        output_file = output_path / f"{format_filename(raw_file.stem)}___ai_processed_transcript.html"
        output_file.write_text(markdown.markdown(final_text), encoding='utf-8')
        
        logging.info(f"Successfully processed {raw_file} -> {output_file}")
        return True
        
    except Exception as e:
        logging.error(f"Error processing {raw_file}: {str(e)}")
        return False
