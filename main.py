# Loyihaning boshlanish nuqtasi
# main.py

from services.books_service import add_books, get_book_by_id, update_book, delete_book
from services.orders_service import create_order, get_all_orders, get_order_by_id, update_order, delete_order

from database import engine, metadata_obj

# barcha modellarni import qilish
from models.users import users
from models.books import books
from models.orders import orders
from models.order_items import order_items

# endi jadval yaratish
metadata_obj.create_all(engine)



def main():
    while True:
        print("\n--- Kitob Do‘koni ---")
        print("1. Yangi kitob qo‘shish")
        print("2. Kitobni ko‘rish (ID bo‘yicha)")
        print("3. Kitobni o‘chirish")
        print("4. Yangi buyurtma qo‘shish")
        print("5. Barcha buyurtmalarni ko‘rish")
        print("0. Chiqish")

        choice = input("Tanlovni kiriting: ")

        if choice == "1":
            title = input("Kitob nomi: ")
            author = input("Muallif: ")
            price = float(input("Narxi: "))
            stock = int(input("Soni: "))
            add_books(title, author, price, stock)
            print("✅ Kitob qo‘shildi!")

        elif choice == "2":
            book_id = int(input("Kitob ID: "))
            book = get_book_by_id(book_id)
            print(book)

        elif choice == "3":
            book_id = int(input("O‘chiriladigan kitob ID: "))
            delete_book(book_id)
            print("❌ Kitob o‘chirildi!")

        elif choice == "4":
            user_id = int(input("Foydalanuvchi ID: "))
            total_price = float(input("Buyurtma summasi: "))
            create_order(user_id, total_price)
            print("🛒 Buyurtma qo‘shildi!")

        elif choice == "5":
            orders = get_all_orders()
            for order in orders:
                print(order)

        elif choice == "0":
            print("Chiqildi 👋")
            break

        else:
            print("❌ Noto‘g‘ri tanlov!")

if __name__ == "__main__":
    main()
