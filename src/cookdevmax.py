from fastapi import FastAPI

app = FastAPI()


@app.get("/hello")
async def say_hello() -> str:
    return "Hello, world!"
