import os
import google.genai as genai
from google.genai import types

from config import AI_API_KEY

client = genai.Client(api_key=AI_API_KEY)

async def translate_text(word: str) -> str:
    response = await client.aio.models.generate_content(
        model="gemini-2.0-flash-lite",
        contents=f"Переведите слово '{word}' Русский<->Английский. Ответьте одним словом без дополнительных пояснений."
    )
    return response.text.strip()

async def generate_image(word: str) -> bytes:
    response = await client.aio.models.generate_images(
        model='imagen-3.0-generate-002',
        prompt=word,
        config=types.GenerateImagesConfig(
            number_of_images=1,
        )
    )
    return response.generated_images[0].image.image_bytes

async def check_translation(word: str, user_translation: str) -> bool:
    response = await client.aio.models.generate_content(
        model="gemini-2.0-flash-lite",
        contents=(
            f"Пользователь ответил, что перевод слова {word} - '{user_translation}'. "
            "Верно это или нет? Ответьте «да» или «нет»."
        )
    )
    answer = response.text.strip().lower()
    return answer.startswith("да")
