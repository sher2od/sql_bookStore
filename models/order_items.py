# Buyurtmadagi mahsulotlar (order_item_id, order_id, book_id, quantity)
from sqlalchemy import Table,Column,Integer,ForeignKey
from database import metadata_obj

order_items = Table(
    "order_items",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("order_id", Integer, ForeignKey("orders.id")),   
    Column("book_id", Integer, ForeignKey("books.id")),
    Column("quantity", Integer, nullable=False)
)
