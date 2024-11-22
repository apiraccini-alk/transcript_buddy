from pathlib import Path

# Base paths
BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "data"

# Input/Output paths
INPUT_PATH = DATA_DIR / "input"
OUTPUT_PATH = DATA_DIR / "output"

# File patterns
INPUT_FILE_PATTERN = "*.docx"

# Chunking settings
DEFAULT_CHUNK_SIZE = 12000
DEFAULT_CHUNK_OVERLAP = 0
