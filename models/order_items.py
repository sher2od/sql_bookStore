# Buyurtmadagi mahsulotlar (order_item_id, order_id, book_id, quantity)
from sqlalchemy import Table,Column,Integer,ForeignKey
from database import metadata_obj

order_items = Table(
    "orders_items",
    metadata_obj,
    Column("order_item_id",Integer,primary_key=True),
    Column("order_id",Integer,ForeignKey("orders.order_id"),nullable=False),
    Column("book_id",Integer,ForeignKey("books.book_id"),nullable=False),
    Column("quantity",Integer,nullable=False)
)