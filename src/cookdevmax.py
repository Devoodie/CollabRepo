from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Subject(BaseModel):
    subject_id: int #primary
    subject_name: str #unique

class Items(BaseModel):
    item_id: int #primary
    subject: int #relational "subject_id"
    publisher: str|None = None
    media_type: str

class page(BaseModel):
    page:int #unique
    book_id:int #relational "item_id"
    content:str #dkhow to implement text
    chapter:str
    publisher:str|None = None #relational "publisher"

@app.get("/hello")
async def say_hello() -> str:
    return "Hello, world!"
