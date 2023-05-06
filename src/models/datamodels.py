from pydantic import BaseModel


class SubjectBase(BaseModel):
    subject_name: str  # unique


class Subject(SubjectBase):
    id: int  # primary

    class Config:
        orm_mode = True


class PageBase(BaseModel):
    page_number: int  # used to solve the problem of page number != place in book
    content: str  # don't know how to implement text
    chapter: str
    book_id: int  # foreign "item_id"


class Page(PageBase):
    id: int  # Primary

    class Config:
        orm_mode = True


class BookBase(BaseModel):
    title: str  # unique
    subject: int  # foreign "subject_id"
    publisher: str | None = None

    class Config:
        orm_mode = True


class Book(BookBase):
    id: int  # primary

    class Config:
        orm_mode = True
