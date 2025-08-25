# Foydalanuvchilar jadvali (user_id, name, email, password)

from sqlalchemy import Table, Column, Integer, String
from database import metadata_obj

users = Table(
    "users",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("email", String, unique=True, nullable=False)
)


