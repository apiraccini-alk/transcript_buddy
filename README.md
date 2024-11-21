# Transcript Buddy

Transcript Buddy is a tool for processing and cleaning transcripts from Teams meetings. It uses language models to clean and format the transcripts into a coherent and readable format.

It was developed to process onboarding lessons transcripts, but the prompts can be adapted for other use cases.

## Setup

1. Clone the repository:
    ```sh
    git clone <repository_url>
    cd transcript_buddy
    ```

2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

3. Create a `.env` file in the root directory and add your API keys (or ask your colleague Alessio Piraccini 😉):
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

- `src/utils/llm.py`: Contains the logic for interacting with language models.
- `src/utils/file_processing.py`: Contains functions for processing files.
- `src/main.py`: The main script to run the processing.
