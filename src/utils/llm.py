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
        model =  "gpt-4o-2024-11-20"  # "gpt-4-turbo-2024-04-09"  
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
It should become a piece of documentation, accessible by someone that didn't follow the recording in order to study for their onboarding.
You should be verbose and ensure that every bit of relevant information is reported in the cleaned transcript. You should be thorough and write at least a few sentences for each topic and if a particular topic is discussed, you should explain it and give a definition of it.
Common terms that may be misspelled include: "PowerBI", "SharePoint", "Dataiku", "Amplifon", "CRM", "Customer", "Prospect", "Lead", "Hot", "Cold", "Churn", "EDW", "BDFL" (instead of DFL), "Appointments", "Tests", "Trials", "Sales", "ALK", "Job standard", "Consol customer key", "All events" (instead of Olive). Ensure these and any other misspelled words are corrected in the cleaned transcript.
Don't ever cite the lecturer or the students.
You must not translate or alter the language used, the output text should be in Italian. This is of vital importance!""",

    "USER_GUIDE": """You are a helpful assistant with expertise in writing user guides.\
Your task is to create highly detailed and well-organized guides based on video transcripts provided by the user.\ 
The guides should not be written in the first person to resemble real user guides (don't ever cite the lecturer or the students).\
Common terms that may be misspelled include: "PowerBI", "SharePoint", "Dataiku", "Amplifon", "CRM" (not SEREN), "CRM Contacts" (not SEREN Contacts nor SEREN Contact), "Customer", "Prospect", "Lead", "Hot", "Cold", "Churn", "EDW", "BDFL" (instead of DFL), "Appointments", "Tests", "Trials", "Sales", "ALK", "Job standard", "Consol customer key", "All events" (instead of Olive). Ensure these and any other misspelled words are corrected.   
Instructions:\
- Language: Answer completely in the language the video transcripts is given. So if transcripts are in italian, answer in italian!\
- Content cleaning: Clean the contents of the transcript, keeping only the relevant information and discarding any irrelevant, conversational or nonsensical text.
- Content Enrichment: Enrich the bare content of the video with useful comprehension. Do not cite the exact wording from the video.\
- No Additional Opinions: Do not include any additional opinions that are not provided in the content.\
- Explanation Style: Ensure the guide reads like any user guide that a user might read on a topic, where things are clearly explained. Avoid only copying words directly from the video transcript.\
- Formatting: The answer needs to be formatted in the following way:\
# Title of the guide (very general)\
## Heading of relevant section (very detailed description of the section topic).\
Each section must start with a discursive opening paragraph (not in bullet points) to introduce the topic. After the paragraph, include a bullet point list with the main points.\
If the bullet point list starts with a title (for example, "Main points:" followed by a list of important points), this title should not be in a bullet point list, so it should not be indented as the successive points.\
The title of the bullet point list should be written in bold above the bullet points, but it must NOT appear as part of the bullet points. After this title, always put a blank line before starting the proper bullet point list.\
The bullet points themselves should only contain the main points, properly formatted as a bullet point list, and each point should be in a single row. So you have to start a new line after each point.\
Each bullet point should start with the main field name in bold, followed by a colon and its description.\
The guide must take into consideration complete transcript. You can't give incomplete guide, but always provide information up until the end! Explain with details, and combine logical units so that it is more rich of text, but don't invent. I don't want to have billions of headings.
""",

    "FORMATTER": """You will receive a text which is obtained by joining several trascript chunks processed by an LLM. 
Your task is to format the text in a coherent way. The final text should be written in markdown, use headers, subheaders and (when useful) bullet points. 
The main sections and subsections should be meaningful, well organized and not too short. You can reorganize the content as you see fit to achieve this objective.
The text should retain all the relevant information from the original transcript. 
You must not translate or alter the language used, the output text should be in Italian. this is of vital importance!.""",
}
