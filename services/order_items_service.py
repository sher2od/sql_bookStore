from sqlalchemy import insert,select,update,delete
from database import engine
from models.order_items import order_items

# Buyurtmaga kitob qoshish
def add_order_item(order_id:int,book_id:int,quantity:int):
    stmt = insert(order_items).values(
        order_id=order_id,
        book_id=book_id,
        quantity=quantity
    )

    with engine.connect() as conn:
        conn.execute(stmt)
        conn.commit()

# Buyurtmadagi barcha kitbni olish
def get_items_by_order(order_id:int):
    stmt = select(order_items).where(order_items.c.order_id == order_id)
    with engine.connect() as conn:
        result = conn.execute(stmt).fetchall()
        return result
    
# Buyurtmadagi kitob sonini yangilash
def update_order_item(item_id:int,new_quantity:int):
    stmt = (
        update(order_items)
        .where(order_items.c.id == item_id)
        .values(quantity=new_quantity)
    )
    with engine.connect() as conn:
        conn.execute(stmt)
        conn.commit()
    
# Buyutrmadn kitobni ochirish
def delete_order_item(item_id:int):
    stmt = delete(order_items).where(order_items.c.id == item_id)
    with engine.connect() as conn:
        conn.execute(stmt)
        conn.commi()