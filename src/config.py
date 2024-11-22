from pathlib import Path

# Base paths
BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "data"

# Input/Output paths
INPUT_PATH = DATA_DIR / "input"
OUTPUT_PATH = DATA_DIR / "output"

# File patterns
INPUT_FILE_PATTERN = "*.docx"

# LLM settings
USE_OPENAI = True

# Chunking settings
DEFAULT_CHUNK_SIZE = 30000
DEFAULT_CHUNK_OVERLAP = 0
