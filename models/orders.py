# Buyurtmalar jadvali (order_id, user_id, total_price, date)


from sqlalchemy import Table,Column,Integer,ForeignKey,Numeric,DateTime
from datetime import datetime
from database import metadata_obj

orders = Table(
    "orders",
    metadata_obj,
    Column("Order_id",Integer,primary_key=True),
    Column("user_id",Integer,ForeignKey("user.id"),nullable=False),
    Column("total_price",Numeric(10,2),nullable=False),
    Column("deta",DateTime,default=datetime.now)
)