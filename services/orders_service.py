from sqlalchemy import select,insert,update,delete
from database import engine
from models.orders import orders


# Yangi buyurtma qoshish
def create_order(user_id,total_price):
    with engine.connect() as conn:
        stmt = insert(orders).values(user_id=user_id,total_price=total_price)
        conn.execute(stmt)
        conn.commit()
    

# Barcha buyurtmani olish
def get_all_orders():
    with engine.connect() as conn:
        stmt = select(orders)
        result = conn.execute(stmt)
        return result
    
# ID orqali bitta buyurtmani olish
def get_order_by_id(order_id):
    with engine.connect() as conn:
        stmt = select(orders).where(orders.c.id == order_id)
        result = conn.execute(stmt)
        return result.fetchone()
    

# Buyurtmani yangilash
def update_order(order_id,new_total_price):
    with engine.connect() as conn:
        stmt = update(orders).where(orders.c.id == order_id).values(total_price=new_total_price)
        conn.execute(stmt)
        conn.commit()


# Buyurtmani o‘chirish
def delete_order(order_id):
    with engine.connect() as conn:
        stmt = delete(orders).where(orders.c.id == order_id)
        conn.execute(stmt)
        conn.commit()

    