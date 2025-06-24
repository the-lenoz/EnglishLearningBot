import aiohttp
import os
from config import AI_API_KEY

async def generate_image(word: str) -> bytes:
    # Placeholder for AI image generation API call
    url = "https://api.example.com/generate"
    headers = {"Authorization": f"Bearer {AI_API_KEY}"}
    payload = {"prompt": word}
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=payload, headers=headers) as resp:
            data = await resp.read()
            return data
