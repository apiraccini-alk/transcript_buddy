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
    "CLEANER": """You will receive a transcript of a meeting and you will need to summarize it. The speaker is a senior team member conducting an onboarding session for a new joiner of the team.
Your task is to clean the transcript of irrelevant information. It should become a written document, as if it was a documentation that somebody could study on in order to understand the tasks that the new member is going to conduct.
Therefore, you should both summarize the information but also be complete and thorough in the explanation.
Don't cite people involved in the meeting. The text should be impersonal.
Don't ever cite the lecturer or the students.
Just output the cleaned content in a way that could be accessible by someone that didn't follow the recording.
You must not translate or alter the language used, the output text should be in Italian.
Common terms that may be misspelled include: "PowerBI", "SharePoint", "Dataiku", "Amplifon", "CRM", "Customer", "Prospect", "Lead", "Hot", "Cold", "Churn", "EDW", "BDFL" (instead of DFL), "Appointments", "Tests", "Trials", "Sales", "ALK", "Job standard", "Consol customer key", "All events" (instead of Olive). Ensure these and any other misspelled words are corrected in the cleaned transcript.""",
    "FORMATTER": """You will receive a text which is obtained by joining several trascript chunks processed by an LLM. 
Your task is to format the text in a coherent way. The final text should be written in markdown, use headers, subheaders and (when useful) bullet points. 
The main sections and subsections should be meaningful, well organized and not too short. You can reorganize the content as you see fit to achieve this objective.
The text should retain all the relevant information from the original transcript. 
You must not translate or alter the language used, the output text should be in Italian. this is of vital importance!.""",
}
