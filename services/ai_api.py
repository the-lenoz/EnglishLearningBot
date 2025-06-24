import os
import google.genai as genai
from config import AI_API_KEY

client = genai.Client()

async def translate_text(word: str) -> str:
    response = await client.generate_content(
        model="gemini",
        prompt=f"Переведите слово '{word}' на русский."
    )
    return response.text.strip()

async def generate_image(word: str) -> bytes:
    response = client.generate_image(
        model="image-bison-001",
        prompt=word,
        image_count=1
    )
    return response.images[0].content

async def check_translation(word: str, user_translation: str) -> bool:
    correct_translation = await translate_text(word)
    response = await client.generate_content(
        model="gemini",
        prompt=(
            f"Правильный перевод слова '{word}' — '{correct_translation}'. "
            f"Пользователь ответил: '{user_translation}'. "
            "Верно это или нет? Ответьте «да» или «нет»."
        )
    )
    answer = response.text.strip().lower()
    return answer.startswith("да")
