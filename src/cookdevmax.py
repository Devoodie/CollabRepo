from fastapi import FastAPI, status
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
import src.models.dataschema as models
from sqlalchemy.orm import Session

app = FastAPI()
# app.mount("/static", StaticFiles(directory="src/web"))


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
async def get_all_books() -> list:
    """Returns a list containing all available books."""
    ...


@app.post("/new/book", status_code=status.HTTP_201_CREATED)
async def create_book(book: models.Book) -> None:
    """Creates a new book. Request body accepts the Book model as json and stores it sa a row in the database."""
    ...


@app.post("/new/page", status_code=status.HTTP_201_CREATED)
async def create_page(page: models.Page) -> None:
    """Creates a new page. Request body accepts the Page model as json and stores it sa a row in the database."""
    ...


@app.post("/new/subject", status_code=status.HTTP_201_CREATED)
async def create_subject(subject: models.Subject) -> None:
    """This could probably just accept a name, and have the ID generated inside the DMBS..."""
    ...


@app.put("/edit/{book_id}", status_code=status.HTTP_200_OK)
async def edit_book(book: models.Book) -> None:
    ...


@app.put("/edit/{page_id}", status_code=status.HTTP_200_OK)
async def edit_page(page: models.Page) -> None:
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


