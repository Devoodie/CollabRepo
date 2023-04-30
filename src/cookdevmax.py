from fastapi import FastAPI

app = FastAPI()


@app.on_event("startup")
async def startup() -> None:
    # do things
    print("All good!")


@app.get("/hello")
async def say_hello() -> str:
    return "Hello, world!"
