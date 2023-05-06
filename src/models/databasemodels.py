from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, Mapped, mapped_column
from src.models.database import Base


class Subject(Base):
    __tablename__ = "subjects"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name: Mapped[str] = mapped_column(unique=True, index=True)
    contents: Mapped[list["Book"]] = relationship()


class Page(Base):
    __tablename__ = "pages"
    id = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    page_number = Column(Integer, unique=True, index=True)
    content = Column(String)
    chapter = Column(String)
    book_id: Mapped[int] = mapped_column(ForeignKey("books.id"))


class Book(Base):
    __tablename__ = "books"
    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    subject = Column(Integer, ForeignKey("subjects.id"))
    title = Column(String, unique=True, index=True)
    publisher = Column(String, nullable=True)
    pages: Mapped[list["Page"]] = relationship()
