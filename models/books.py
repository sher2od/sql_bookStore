# Kitoblar jadvali (book_id, title, author, price, stock)

from sqlalchemy import Table,Column,Integer,String
from database import metadata_obj

books = Table(
    "books",
    metadata_obj,
    Column("book_id",Integer,primary_key=True),
    Column("title",String(199),nullable=False),
    Column("auther",String(100),nullable=False),
    Column("price",float,nullable=False),
    Column("stock",Integer,nullable=False,default=0)
)