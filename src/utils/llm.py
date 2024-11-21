from pathlib import Path
import os
from groq import Groq
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


def llm(system_prompt: str, user_text: str, oai: bool = True) -> str:
    """
    Generate a response from the language model based on the provided prompts.

    Args:
        system_prompt (str): The system prompt to guide the model.
        user_text (str): The user input text.
        oai (bool, optional): Flag to use OpenAI or Groq. Defaults to True.

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
    "CLEANER": """You are an expert transcript cleaner. Your will receive a segment of a transcript from a Teams meeting, where a senior team member is conducting an onboarding session for new joiners.
Your task is to clean the contents of the transcript, keeping only the relevant information and discarding any irrelevant, conversational or nonsensical text.
You should be verbose and ensure that every bit of relevant information is reported in the cleaned transcript.
Common terms that may be misspelled include: "PowerBI", "SharePoint", "Dataiku", "Amplifon", "CRM", "Customer", "Prospect", "Lead", "Hot", "Cold", "Churn", "EDW", "BDFL" (instead of DFL), "Appointments", "Tests", "Trials", "Sales", "ALK", "Job standard", "Consol customer key", "All events" (instead of Olive). Ensure these and any other misspelled words are corrected in the cleaned transcript.
Don't ever cite the lecturer or the students, just output the cleaned content in a way that could be accessible by someone that didn't follow the recording.
You must not translate or alter the language used, the output text should be in Italian. this is of vital importance!""",
    "FORMATTER": """You will receive a text which is obtained by joining several trascript chunks processed by an LLM. 
Your task is to format the text in a coherent way. The final text should be written in markdown, use headers, subheaders and (when useful) bullet points. 
The sections and subsections should be meaningful, well organized and not too short. You can reorganize the content as you see fit to achieve this objective.
The text should retain all the relevant information from the original transcript. 
You must not translate or alter the language used, the output text should be in Italian. this is of vital importance!.""",
}
