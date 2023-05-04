from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database import Base


class Subject(Base):
    __tablename__ = "subjects"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    bookz = relationship("Book", back_populates="subject")


class Page(Base):
    __tablename__ = "pages"
    id = Column(Integer, primary_key=True, index=True)
    page_number = Column(Integer, primary_key=True, index=True)
    book_id = Column(Integer, ForeignKey("Book.book_id"))
    content = Column(String)
    chapter = Column(String)
    book = relationship("Book", back_populates="pages")


class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, index=True)
    subject = Column(String)
    pages = relationship("Page", back_populates="book")
