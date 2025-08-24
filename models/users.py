# Foydalanuvchilar jadvali (user_id, name, email, password)

from sqlalchemy import Table,Column,Integer,String
from database import metadata_obj

users = Table(
    "users",
    metadata_obj,
    Column("id",Integer,primary_key=True),
    Column("name",String(100),nullable=False),
    Column("email",String(120),unique=True,nullable=False),
    Column("password",String(200),nullable=False)
)