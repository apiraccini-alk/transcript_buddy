from pathlib import Path
import os
from groq import Groq
from openai import OpenAI
from dotenv import load_dotenv

from config import USE_OPENAI

load_dotenv()


def llm(system_prompt: str, user_text: str, oai: bool = USE_OPENAI) -> str:
    """
    Generate a response from the language model based on the provided prompts.

    Args:
        system_prompt (str): The system prompt to guide the model.
        user_text (str): The user input text.
        oai (bool, optional): Flag to use OpenAI or Groq.

    Returns:
        str: The generated response from the language model.
    """
    if oai:
        client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
        model = "gpt-4o"
    else:
        client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
        model = "llama-3.1-70b-versatile"

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": system_prompt,
            },
            {
                "role": "user",
                "content": user_text,
            },
        ],
        model=model,
        temperature=0,
        max_tokens=None,
    )

    return chat_completion.choices[0].message.content


prompts = {
    "TOC": """You will receive a text, which is a transcript of a Teams meeting, where a senior team member is conducting an onboarding session for new joiners.
Your task is to create a table of contents. Therefore, you need to understand the structure of the document and the major divisions like chapters or main sections.
Then, if there are other subtopics corraleted, you should recognize smaller divisions within those sections, such as subsections or subheadings.
Keep only the table of contents. Don't say anything else. Keep everything in Italian. Format it in markdown.
""",



    "CLEANER": """You are an expert transcript cleaner. Your will receive a segment of a transcript from a Teams meeting, where a senior team member is conducting an onboarding session for new joiners.
Your task is to clean the contents of the transcript, keeping only the relevant information and discarding any irrelevant, conversational or nonsensical text.
It should become a piece of documentation, accessible by someone that didn't follow the recording in order to study for their onboarding.
You should be verbose and ensure that every bit of relevant information is reported in the cleaned transcript. You should be thorough and write at least a few sentences for each topic and if a particular topic is discussed, you should explain it and give a definition of it.
Common terms that may be misspelled include: "PowerBI", "SharePoint", "Dataiku", "Amplifon", "CRM", "Customer", "Prospect", "Lead", "Hot", "Cold", "Churn", "EDW", "BDFL" (instead of DFL), "Appointments", "Tests", "Trials", "Sales", "ALK", "Job standard", "Consol customer key", "All events" (instead of Olive). Ensure these and any other misspelled words are corrected in the cleaned transcript.
Don't ever cite the lecturer or the students.
You must not translate or alter the language used, the output text should be in Italian. This is of vital importance!""",
    
    
    "FORMATTER": """You will receive a text, which is a transcript of a Teams meeting, where a senior team member is conducting an onboarding session for new joiners.
Your task is to perform the following actions:
1. Clean the text, keeping only the relevant information and discarding any irrelevant, conversational or nonsensical text.
2. Correct any misspelled words; common terms that may be misspelled include: "PowerBI", "SharePoint", "Dataiku", "Amplifon", "CRM", "Customer", "Prospect", "Lead", "Hot", "Cold", "Churn", "EDW", "BDFL" (instead of DFL), "Appointments", "Tests", "Trials", "Sales", "ALK", "Job standard", "Consol customer key", "All events" (instead of Olive). Ensure these and any other misspelled words are corrected in the cleaned transcript.
3. Format the text in markdown following the provided table of contents.
The text should retain all the relevant information from the original transcript. 
You must not translate or alter the language used, the output text should be in Italian. this is of vital importance!.
Here is the table of contents:
{toc}""",
}
