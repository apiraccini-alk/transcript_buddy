# Transcript Buddy

Transcript Buddy is a tool for processing and cleaning transcripts from Teams meetings. It uses language models to clean and format the transcripts into a coherent and readable format.

It was developed to process onboarding lessons transcripts, but the prompts can be adapted for other use cases.

## Features

- Processes Microsoft Teams meeting transcripts (`.docx` files)
- Cleans and formats transcripts using AI language models (OpenAI/Groq)
- Handles multiple files in batch processing
- Maintains original content while improving readability
- Generates clean, structured output files

## Setup

1. Clone the repository:
    ```sh
    git clone <repository_url>
    cd transcript_buddy
    ```

2. Create and activate a virtual environment (recommended):
    ```sh
    python -m venv .venv
    .venv\Scripts\activate  # On Windows
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the root directory and add your API keys (or ask your colleague Alessio Piraccini 😉):
    ```env
    OPENAI_API_KEY=your_openai_api_key
    GROQ_API_KEY=your_groq_api_key
    ```

## Usage

1. Create the necessary directories:
    ```sh
    mkdir -p data/input
    ```

2. Place your `.docx` files in the `data/input` directory.

3. Run the main script to process the files:
    ```sh
    python src/main.py
    ```

4. The processed transcripts will be saved in the `data/output` directory.

## Project Structure

```
transcript_buddy/
├── data/
│   ├── input/     # Place input .docx files here
│   └── output/    # Processed transcripts are saved here
├── src/
│   ├── utils/
│   │   ├── file_processing.py  # File handling functions
│   │   └── llm.py             # Language model interactions
│   ├── config.py              # Configuration settings
│   └── main.py               # Main processing script
├── .env                      # Environment variables (API keys)
├── .gitignore
├── README.md
└── requirements.txt
```

## Dependencies

- `python-docx`: For reading and writing Word documents
- `tiktoken`: Token counting for OpenAI models
- `markdown`: Markdown processing
- `python-dotenv`: Environment variable management
- `openai`: OpenAI API client
- `requests`: HTTP client for API calls

## Error Handling

The application includes comprehensive error handling:
- Logs all operations with timestamps
- Provides clear error messages for common issues
- Continues processing remaining files if one file fails
- Creates detailed processing summaries
