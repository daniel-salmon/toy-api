import asyncio
import random

from fastapi import FastAPI
from typing import Optional

from .toy_names import adjectives, nouns


app = FastAPI()


@app.get("/toys/{toy_id}")
async def get_toy(toy_id: int, delay: Optional[int] = 0):
    toy_name = f"{random.choice(adjectives)}-{random.choice(nouns)}"
    if delay > 0:
        await asyncio.sleep(delay)
    return {"id": toy_id, "name": toy_name}
