from sqlalchemy import insert,select
from database import engine
from models.users import users


def create_user(name:str,email:str,password:str):
    """Yangi foydalanuvchi qoshish"""
    stmt = insert(users).values(
        name=name,
        email=email,
        password=password
    )

    with engine.connect() as conn:
        conn.execute(stmt)
        conn.commit()
        print("✅ Foydalanuvchi muvaffaqiyatli qo'shildi!")

def get_all_users():
    """Barcha foydalanuvchilarni olish"""
    stmt = select(users)
    with engine.connect() as conn:
        result = conn.execute(stmt)
        return result.fetchall()
    

   #    https://chatgpt.com/c/68a80c3f-e938-8320-a741-99b1e0ab789c