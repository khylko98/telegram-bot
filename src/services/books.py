from db import Base, db_context

from sqlalchemy import Column, Integer, String, Text

from logging_config import setup_logger


logger = setup_logger()


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    title = Column(String(100), unique=True, nullable=False)
    img_link = Column(Text, nullable=False)
    bg_img_link = Column(Text, nullable=False)

    @classmethod
    def get_by_title(cls, session, title):
        return session.query(cls).filter(cls.title == title).first()


def insert_book(title, img_link, bg_img_link):
    try:
        with db_context() as db:
            new_book = Book(title=title, img_link=img_link, bg_img_link=bg_img_link)
            db.add(new_book)
            db.commit()
            db.refresh(new_book)
            return True
    except Exception as error:
        logger.warning("Error inserting book:", error)
        return False


def get_book_by_title(title):
    try:
        with db_context() as db:
            book = Book.get_by_title(db, title)
            return book
    except Exception as error:
        logger.warning("Error getting book:", error)
        return None
