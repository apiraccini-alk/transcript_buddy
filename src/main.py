from pathlib import Path
import logging

from utils.file_processing import process_file

logging.basicConfig(level=logging.INFO)


if __name__ == "__main__":

    input_path = Path("data/input")
    output_path = Path("data/output")
    output_path.mkdir(parents=True, exist_ok=True)

    raw_files = list(input_path.glob("*.docx"))

    for raw_file in raw_files:
        process_file(raw_file, output_path)
