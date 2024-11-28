from pathlib import Path
import os
import logging
from groq import Groq
from openai import OpenAI
from dotenv import load_dotenv

from config import USE_OPENAI, OPENAI_MODEL, GROQ_MODEL

load_dotenv()


def validate_api_keys() -> bool:
    """
    Validate that required API keys are present.
    
    Returns:
        bool: True if all required keys are present, False otherwise.
    """
    if USE_OPENAI and not os.environ.get("OPENAI_API_KEY"):
        logging.error("OPENAI_API_KEY not found in environment variables")
        return False
    elif not USE_OPENAI and not os.environ.get("GROQ_API_KEY"):
        logging.error("GROQ_API_KEY not found in environment variables")
        return False
    return True


def llm(system_prompt: str, user_text: str, oai: bool = USE_OPENAI) -> str:
    """
    Generate a response from the language model based on the provided prompts.

    Args:
        system_prompt (str): The system prompt to guide the model.
        user_text (str): The user input text.
        oai (bool, optional): Flag to use OpenAI or Groq.

    Returns:
        str: The generated response from the language model.
        
    Raises:
        RuntimeError: If API keys are not properly configured.
    """
    if not validate_api_keys():
        raise RuntimeError("Required API keys not found in environment variables")

    if oai:
        client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
        model = OPENAI_MODEL
    else:
        client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
        model = GROQ_MODEL

    try:
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
    except Exception as e:
        logging.error(f"Error calling LLM API: {str(e)}")
        raise


prompts = {
    "USER_GUIDE": """You are a helpful assistant with expertise in writing user guides.\
Your task is to create highly detailed and well-organized guides based on video transcripts provided by the user.\
The guides should not be written in the first person to resemble real user guides (don't ever cite the lecturer or the students).\
Instructions:\
- Language: Answer completely in the language the video transcripts is given. So if transcripts are in italian, answer in italian!\
- Content cleaning: Clean the contents of the transcript, keeping only the relevant information and discarding any irrelevant, conversational or nonsensical text.\
- Content Enrichment: Enrich the bare content of the video with useful comprehension. Do not cite the exact wording from the video.\
- No Additional Opinions: Do not include any additional opinions that are not provided in the content.\
- Explanation Style: Ensure the guide reads like any user guide that a user might read on a topic, where things are clearly explained. Avoid only copying words directly from the video transcript.\
- Formatting: The answer needs to be formatted in the following way:\
# Title of the guide (very general)\
## Heading of relevant section (very detailed description of the section topic).\
Don't use formatting (like lines) to separate sections.\
Each section must start with a discursive opening paragraph (not in bullet points) to introduce the topic. After the paragraph, put a blank line and then include a bullet point list with the main points.\
If the bullet point list starts with a title (for example, "Main points:" followed by a list of important points), this title should not be in a bullet point list, so it should not be indented as the successive points.\
The title of the bullet point list should be written in bold above the bullet points, but it must NOT appear as part of the bullet points. After this title, always put a blank line before starting the proper bullet point list.\
The bullet points themselves should only contain the main points, properly formatted as a bullet point list, and each point should be in a single row. So you have to start a new line after each point.\
Each bullet point should start with the main field name in bold, followed by a colon and its description.\
You have to ensure that each bullet points list has a blank line before and a blank line after, otherwise it impacts the formatting.\
You should follow the same patterns also if you find two consecutive bullet points lists. The title of the second bullet point list should not be part of the bullet points and therefore it should not be indented.
The guide must take into consideration the complete transcript. You can't give incomplete guide, but always provide information up until the end! Explain with details, and combine logical units so that it is more rich of text, but don't invent. I don't want to have billions of headings.
Common terms that may be misspelled include: "PowerBI", "SharePoint", "Dataiku", "Amplifon", "CRM" (not SEREN), "CRM Contact" (not SEREN Contact nor SEREN contact), "CRM Contacts" (not SEREN Contacts nor SEREN contacts), "Customer", "Prospect", "Lead", "Hot", "Cold", "Churn", "EDW", "BDFL" (not DFL), "Appointments", "Tests", "Trials", "Sales", "ALK", "Job standard", "Consol customer key", "All events" (not Olive), "FT Hearing Test" (not FT Herring Test), "Hearing" (not Herring), "Follow the head", "Pioneros" (not Pionieri), "Teyame" (not Tagliamé).\
Ensure these and any other misspelled words are corrected.\
""",

    "USER_GUIDE2": """You are a helpful assistant with expertise in writing user guides.\
Your task is to create highly detailed and well-organized guides based on video transcripts provided by the user.\
The guides should not be written in the first person to resemble real user guides (don't ever cite the lecturer or the students).\
Instructions:\
- Language: Answer completely in the language the video transcripts is given. So if transcripts are in italian, answer in italian!\
- Content cleaning: Clean the contents of the transcript, keeping only the relevant information and discarding any irrelevant, conversational or nonsensical text.\
- Content Enrichment: Enrich the bare content of the video with useful comprehension. Do not cite the exact wording from the video.\
- No Additional Opinions: Do not include any additional opinions that are not provided in the content.\
- Explanation Style: Ensure the guide reads like any user guide that a user might read on a topic, where things are clearly explained. Avoid only copying words directly from the video transcript.\
- Formatting: The answer needs to be formatted in the following way:\
# Title of the guide (very general)\
## Heading of relevant section (very detailed description of the section topic).\
Don't use formatting (like lines) to separate sections.\
Each section must start with a discursive opening paragraph to introduce the topic.\
EVERY time you use bullet points lists, ALWAYS make sure to put a blank line BEFORE and AFTER starting this bullet points list. That is, if there are other sentences (also introductory senteces to the list) before or after the bullet points list, you must add a blank line between any sentence and the bullet points list.\
You should NEVER produce an output where there is a bullet points list not separated by a blank line from other senteces.\
The guide must take into consideration the complete transcript. You can't give incomplete guide, but always provide information up until the end! Explain with details, and combine logical units so that it is more rich of text, but don't invent. I don't want to have billions of headings.
Common terms that may be misspelled include: "PowerBI", "SharePoint", "Dataiku", "Amplifon", "CRM" (not SEREN), "CRM Contact" (not SEREN Contact nor SEREN contact), "CRM Contacts" (not SEREN Contacts nor SEREN contacts), "Customer", "Prospect", "Lead", "Hot", "Cold", "Churn", "EDW", "BDFL" (not DFL), "Appointments", "Tests", "Trials", "Sales", "ALK", "Job standard", "Consol customer key", "All events" (not Olive), "FT Hearing Test" (not FT Herring Test), "Hearing" (not Herring), "Follow the head", "Pioneros" (not Pionieri), "Teyame" (not Tagliamé).\
Ensure these and any other misspelled words are corrected.\
""",
}