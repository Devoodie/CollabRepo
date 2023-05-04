from pydantic import BaseModel


class Subject(BaseModel):
    subject_id: int  # primary
    subject_name: str  # unique


class Page(BaseModel):
    page_id: int  # unique
    page_number: int  # used to solve the problem of page number != place in book
    book_id: int  # foreign "item_id"
    content: str  # don't know how to implement text
    chapter: str
    publisher: str | None = None  # foreign "publisher"

    class Config:
        orm_mode = True


class Book(BaseModel):
    book_id: int  # primary
    subject: int  # foreign "subject_id"
    publisher: str | None = None
    # pages: list[Page.page_id]
    pages: list[Page.page_id]  # Page.page_id
