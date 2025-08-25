# Kitoblar jadvali (book_id, title, author, price, stock)

from sqlalchemy import Table,Column,Integer,String,Numeric
from database import metadata_obj

books = Table(
    "books",
    metadata_obj,
    Column("id", Integer, primary_key=True),  
    Column("title", String, nullable=False),
    Column("author", String, nullable=False),
    Column("price", Numeric, nullable=False),
    Column("stock", Integer, nullable=False, default=0)  # qo‘shildi
)
