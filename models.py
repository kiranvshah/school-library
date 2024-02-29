from sqlalchemy import Column, Integer, String, Date, Table, ForeignKey, UniqueConstraint
from sqlalchemy.orm import DeclarativeBase, relationship


class Base(DeclarativeBase):
    pass


book_author = Table('book_author',
                    Base.metadata,
                    Column('id', Integer, primary_key=True),
                    Column('book_id', ForeignKey('book.id')),
                    Column('author_id', ForeignKey('author.id')),
                    UniqueConstraint('book_id', 'author_id'),
                    )


class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    isbn = Column(Integer, nullable=False, unique=True)
    num_pages = Column(Integer)
    publication_date = Column(Date)
    publisher_id = Column(Integer, ForeignKey('publisher.id'), nullable=False)
    authors = relationship('Author', secondary=book_author, back_populates='works')


class Author(Base):
    __tablename__ = 'author'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    works = relationship('Book', secondary=book_author, back_populates='authors')


class Publisher(Base):
    __tablename__ = 'publisher'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
