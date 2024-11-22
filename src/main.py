import sys
import logging
from pathlib import Path

from config import INPUT_PATH, OUTPUT_PATH, INPUT_FILE_PATTERN
from utils.file_processing import process_file


def setup_logging():
    """Configure logging with a specific format."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )


def main():
    """Main function to process transcript files."""
    try:
        # Ensure output directory exists
        OUTPUT_PATH.mkdir(parents=True, exist_ok=True)
        
        # Get list of input files
        raw_files = list(INPUT_PATH.glob(INPUT_FILE_PATTERN))
        
        if not raw_files:
            logging.warning(f"No {INPUT_FILE_PATTERN} files found in {INPUT_PATH}")
            return
        
        logging.info(f"Found {len(raw_files)} files to process")
        
        # Process each file
        success_count = 0
        for raw_file in raw_files:
            if process_file(raw_file, OUTPUT_PATH):
                success_count += 1
        
        # Log summary
        logging.info(f"Processing complete. Successfully processed {success_count}/{len(raw_files)} files")
        
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    setup_logging()
    main()
