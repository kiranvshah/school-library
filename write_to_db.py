from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import Book, Author, Publisher

books = [
    Book(title='Harry Potter and the Philosopher\'s Stone', isbn=12345, num_pages=200),
    Book(title='War and Peace', isbn=343, num_pages=10_000),
    Book(title='Murder on the Orient Express', isbn=2934, num_pages=305),
    Book(title='The Hitchhiker\'s Guide to the Galaxy', isbn=92384, num_pages=900),
    Book(title='Spare', isbn=238, num_pages=30),
]

books[0].authors.append(Author(name='JK Rowling'))
books[1].authors.append(Author(name='Leo Tolstoy'))
books[2].authors.append(Author(name='Agatha Christie'))
books[3].authors.append(Author(name='Douglas Adams'))
books[4].authors.append(Author(name='Prince Harry'))

HarperCollins = Publisher(name='HarperCollins')
Penguin = Publisher(name='Penguin')
Bloomsbury = Publisher(name='Bloomsbury')

books[0].publisher_id = Bloomsbury.id
books[1].publisher_id = Penguin.id
books[2].publisher_id = HarperCollins.id
books[3].publisher_id = Penguin.id
books[4].publisher_id = HarperCollins.id

engine = create_engine('sqlite:///library.sqlite', echo=True)

with Session(engine) as sess:
    sess.add_all(books)
    sess.commit()
