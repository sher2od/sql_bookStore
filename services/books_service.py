from sqlalchemy import insert,select,update,delete
from database import engine
from models.books import books


# Yangi kitob qoshish
def add_books(title,author,price,stock):
    stmt = insert(books).values(
        title=title,
        author=author,
        price=price,
        stock=stock
    )
    with engine.connect() as conn:
        conn.execute(stmt)
        conn.commit


# Barcha kitoblarni olish
def get_book_by_id(book_id):
    stmt = select(books).where(books.c.book_id == book_id)
    with engine.connect() as conn:
        result = conn.execute(stmt).fetchall()
        return result


# KITOBNI yangilash
def update_book(book_id,**kwargs):
    stmt = update(books).where(books.c.book_id == book_id).values(**kwargs)
    with engine.connect() as conn:
        conn.execute(stmt)
        conn.commit()

# Kitobni ochirish
def delete_book(book_id):
    stmt = delete(books).where(books.c.book_id == book_id)
    with engine.connect() as conn:
        conn.execute(stmt)
        conn.commit()


        # https://chatgpt.com/c/68a80c3f-e938-8320-a741-99b1e0ab789c