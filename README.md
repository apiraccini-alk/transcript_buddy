# Transcript Buddy

Transcript Buddy is a tool for processing and cleaning transcripts from Teams meetings. It uses language models to clean and format the transcripts into a coherent and readable format.

It was developed to process onboarding lessons transcripts, but the prompts can be adapted for other use cases.

## Features

- Processes Microsoft Teams meeting transcripts (`.docx` files)
- Cleans and formats transcripts using AI language models (OpenAI/Groq)
- Handles multiple files in batch processing
- Maintains original content while improving readability
- Generates clean, structured output files
- Token limit validation to ensure model compatibility
- Support for both OpenAI and Groq language models

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

## Configuration

The application can be configured through the `config.py` file:

- `USE_OPENAI`: Toggle between OpenAI (True) and Groq (False) models
- `MAX_TOKENS`: Maximum token limit for text processing (default: 128k)
- `OPENAI_MODEL`: OpenAI model to use (default: "gpt-4o-2024-11-20")
- `GROQ_MODEL`: Groq model to use (default: "llama-3.1-70b-versatile")

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

## Output Format

The processed transcripts are saved as HTML files with:
- A header indicating the source (Amplifon CoE)
- The cleaned and formatted transcript content
- A disclaimer about AI-generated content
- Markdown formatting for better readability

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
- `groq`: Groq API client

## Error Handling

The application includes comprehensive error handling:
- Logs all operations with timestamps
- Validates API keys before processing
- Checks token limits to prevent model errors
- Provides clear error messages for common issues
- Continues processing remaining files if one file fails
- Creates detailed processing summaries

## Troubleshooting

Common issues and solutions:

1. **Missing API Keys**
   - Ensure your `.env` file exists and contains the required API keys
   - Check that the API keys are valid and not expired

2. **Token Limit Exceeded**
   - The file content exceeds the maximum token limit (128k)
   - Consider splitting the file into smaller parts

3. **File Format Issues**
   - Ensure input files are in `.docx` format
   - Check that files are not corrupted or password-protected

4. **Processing Errors**
   - Check the logs for specific error messages
   - Verify that the input file is a valid Teams transcript
   - Ensure you have an active internet connection

For any other issues, please check the logs or contact the maintainers.
