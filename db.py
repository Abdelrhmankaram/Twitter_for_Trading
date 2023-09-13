import sqlite3
import traceback
from User import User
from Product import Product

conn = sqlite3.connect('main_db.db')
# returns None if user is not found else returns user_id
def validate_login(user_name: str, password: str):
    cur = conn.cursor()
    try:
        res = cur.execute("""
            SELECT user_id FROM user WHERE user_name=? AND password=?
        """, (user_name, password))

        return res.fetchone()

    except Exception as e:
        print("An exception occurred:", e)
        traceback.print_exc()

    cur.close()
    return None


def check_user_name_available(user_name: str) -> bool:
    cur = conn.cursor()
    try:
        res = cur.execute("""
            SELECT * FROM user WHERE user_name=?
        """, (user_name,))

        return res.fetchone() is None

    except Exception as e:
        print("An exception occurred:", e)
        traceback.print_exc()

    cur.close()
    return False


# returns None if error occured else returns user_id
def add_user(user: User) -> int | None:
    cur = conn.cursor()
    try:
        res = cur.execute("""
                        
            INSERT INTO user
            (user_name, password, name, email, phone) 
            VALUES
            (?, ?, ?, ?, ?)

        """, (user.user_name, user.password, user.name, user.email, user.phone))  # Pass parameters as a tuple

    except Exception as e:
        print("An exception occurred:", e)
        traceback.print_exc()
    
    conn.commit()
    cur.close()

    return cur.lastrowid


# returns None if error occured else returns product_id
def add_product(product: Product) -> int | None:
    cur = conn.cursor()
    
    try:
        res = cur.execute("""
                        
            INSERT INTO product
            (user_id, product_name, category, picture, description, price, status)
            VALUES
            (?, ?, ?, ?, ?, ?, ?)

        """, (product.user_id, product.product_name, product.category, product.picture, product.description, product.price, product.status))  # Pass parameters as a tuple

    except Exception as e:
        print("An exception occurred:", e)
        traceback.print_exc()
    
    conn.commit()
    cur.close()

    return cur.lastrowid



def update_product(product: Product, product_id):
    cur = conn.cursor()
    
    try:
        res = cur.execute("""
                        
            UPDATE product
            SET product_name = ?, 
                category = ?, 
                picture = ?,
                description = ?, 
                price = ?, 
                status = ?
                          
            WHERE product_id = ?

        """, (product.product_name, product.category, product.picture, product.description, product.price, product.status, product_id))  # Pass parameters as a tuple

    except Exception as e:
        print("An exception occurred:", e)
        traceback.print_exc()
    
    conn.commit()
    cur.close()



def get_product(product_id: int) -> Product | None:
    cur = conn.cursor()
    try:
        res = cur.execute("""
            SELECT * FROM product WHERE product_id=?
        """, (product_id,))
       
        return Product.create_object(res.fetchone())


    except Exception as e:
        print("An exception occurred:", e)
        traceback.print_exc()

    cur.close()

    return None



def get_all_products() -> list | None:
    cur = conn.cursor()
    try:
        res = cur.execute("""
            SELECT * FROM product
        """)
       
        products = []
        for product in res.fetchall():
            products.append(Product.create_object(product))

        return products


    except Exception as e:
        print("An exception occurred:", e)
        traceback.print_exc()

    cur.close()



def get_product_by_category(category: str) -> list | None:
    cur = conn.cursor()
    try:
        res = cur.execute("""
            SELECT * FROM product WHERE category=?
        """, (category,))
       
        products = []
        for product in res.fetchall():
            products.append(Product.create_object(product))

        return products


    except Exception as e:
        print("An exception occurred:", e)
        traceback.print_exc()

    cur.close()



def delete_product(product_id: int):
    cur = conn.cursor()
    try:
        res = cur.execute("""
            DELETE FROM product WHERE product_id=?
        """, (product_id,))

    except Exception as e:
        print("An exception occurred:", e)
        traceback.print_exc()

    conn.commit()
    cur.close()

def delete_product2():
    cur = conn.cursor()
    try:
        res = cur.execute('''
            DELETE FROM product
        ''')

    except Exception as e:
        print("An exception occurred:", e)
        traceback.print_exc()

    conn.commit()
    cur.close()
def get_products_by_user(user_id):
    cur = conn.cursor()
    try:
        res = cur.execute("""
            SELECT * FROM product WHERE user_id=?
        """, (user_id,))
       
        products = []
        for product in res.fetchall():
            products.append(Product.create_object(product))

        return products


    except Exception as e:
        print("An exception occurred:", e)
        traceback.print_exc()

    cur.close()

def get_phone(user_id):
    cur = conn.cursor()
    try:
        res = cur.execute("""
            SELECT phone FROM user WHERE user_id=?
        """, (user_id,))

        return res.fetchone()[0]

    except Exception as e:
        print("An exception occurred:", e)
        traceback.print_exc()

    cur.close()

def main():
    delete_product(6)
    
main()
    
    
#main()

# cur.execute("""           
#     CREATE TABLE user (
#         user_id INTEGER PRIMARY KEY,
#         user_name TEXT,
#         password TEXT,
#         name TEXT,
#         email TEXT,
#         phone TEXT
#     );
    
# """)

# conn.commit()



 

# conn.commit()

# conn.close()
