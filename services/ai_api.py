import os
import google.genai as genai
from config import AI_API_KEY

client = genai.Client()

async def translate_text(word: str) -> str:
    response = client.generate_text(
        model="chat-bison-001",
        prompt=f"Translate the following English word to Russian: '{word}'"
    )
    return response.result.strip()

async def generate_image(word: str) -> bytes:
    response = client.generate_image(
        model="image-bison-001",
        prompt=word,
        image_count=1
    )
    return response.images[0].content

async def check_translation(word: str, user_translation: str) -> bool:
    response = client.generate_text(
        model="chat-bison-001",
        prompt=(
            f"Given the English word '{word}' and its correct Russian translation "
            f"'{await translate_text(word)}', is '{user_translation}' correct? "
            "Answer 'yes' or 'no'."
        )
    )
    answer = response.result.strip().lower()
    return answer.startswith("yes")
