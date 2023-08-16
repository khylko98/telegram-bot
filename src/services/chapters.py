from db import Base, db_context

from sqlalchemy import Column, Integer, String, Text, ForeignKey

from logging_config import setup_logger


logger = setup_logger()


class Chapter(Base):
    __tablename__ = "chapters"

    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey("books.id"), nullable=False)
    title = Column(String(100), nullable=False)
    audio_link = Column(Text, nullable=False)

    @classmethod
    def get_by_title(cls, session, title):
        return session.query(cls).filter(cls.title == title).first()


def insert_chapter(book_id, title, audio_link):
    try:
        with db_context() as db:
            new_chapter = Chapter(book_id=book_id, title=title, audio_link=audio_link)
            db.add(new_chapter)
            db.commit()
            db.refresh(new_chapter)
            return True
    except Exception as error:
        logger.warning("Error inserting chapter:", error)
        return False


def get_chapter_by_title(title):
    try:
        with db_context() as db:
            chapter = Chapter.get_by_title(db, title)
            return chapter
    except Exception as error:
        logger.warning("Error getting chapter:", error)
        return None
