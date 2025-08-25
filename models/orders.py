# Buyurtmalar jadvali (order_id, user_id, total_price, date)


from sqlalchemy import Table, Column, Integer, String, ForeignKey, DateTime
from database import metadata_obj
import datetime

orders = Table(
    "orders",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("user_id", Integer, ForeignKey("users.id")),
    Column("status", String, nullable=False)
)
