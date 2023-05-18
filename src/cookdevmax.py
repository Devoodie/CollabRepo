from fastapi import FastAPI, status, Depends, HTTPException
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from sqlalchemy import select
from sqlalchemy.orm import Session
from src.models import dataschema, databasemodels
from src.models.database import SessionLocal, engine

databasemodels.Base.metadata.create_all(bind=engine)

app = FastAPI()
# app.mount("/static", StaticFiles(directory="src/web"))


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.on_event("startup")
async def startup() -> None:
    # connect to database
    # run a test
    print("All good!")


@app.get("/")
async def root() -> RedirectResponse:
    return RedirectResponse("/static/home.html")


@app.get("/hello")
async def say_hello() -> str:
    return "Hello, world!"


@app.get("/subjects")
async def return_all_subjects() -> list:
    """Returns a list containing all available subjects."""
    ...


@app.get("/books")
async def get_all_books(db: Session = Depends(get_db)) -> list:
    """Returns a list containing all available books."""
    result = db.execute(select(databasemodels.Book))
    booklist = []
    for book in result:
        booklist.append(book.id)
    return booklist


@app.post("/new/book", status_code=status.HTTP_201_CREATED)
async def create_book(book: dataschema.BookBase, db: Session = Depends(get_db)) -> None:
    """Creates a new book. Request body accepts the Book model as json and stores it sa a row in the database."""
    db_book = databasemodels.Book(subject=book.subject, title=book.title, publisher=book.publisher)
    db.add(db_book)
    db.commit()


@app.post("/new/page", status_code=status.HTTP_201_CREATED)
async def create_page(page: dataschema.Page) -> None:
    """Creates a new page. Request body accepts the Page model as json and stores it sa a row in the database."""
    ...


@app.post("/new/subject", status_code=status.HTTP_201_CREATED)
async def create_subject(subject: dataschema.Subject) -> None:
    """This could probably just accept a name, and have the ID generated inside the DMBS..."""
    ...


@app.put("/edit/{book_id}", status_code=status.HTTP_200_OK)
async def edit_book(book: dataschema.Book) -> None:
    ...


@app.put("/edit/{page_id}", status_code=status.HTTP_200_OK)
async def edit_page(page: dataschema.Page) -> None:
    """Edits a page, accepting the Page model and updating the row. """
    # TODO: Decide if this should actually return the original page, for some kind of last minute undo/revert function
    ...
# Save for when auth/auth is figured out
# @app.delete("/{book_id}")
# @app.delete("/{book_id}/{page_id}")
# @app.delete("/{subject_id}")


@app.get("/status", status_code=status.HTTP_200_OK)
async def health_check() -> dict:
    # Check connection to database
    # check latency to pages table
    # return json
    ...
