from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/hello")
async def say_hello() -> str:
    return "Hello, world!"
