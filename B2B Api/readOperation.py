import sqlite3

def authenticate_user(email, password):
    conn = sqlite3.connect("mymedicalshop.db")
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM Users WHERE email = ? AND password = ?
    ''',(email, password))
    user = cursor.fetchone()
    conn.close()
    return user

def find_user_by_email(email):
    conn = sqlite3.connect("mymedicalshop.db")
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM Users WHERE email = ?
    ''',(email,))
    user = cursor.fetchone()
    conn.close()
    return user


def get_All_Users():
    conn = sqlite3.connect("mymedicalshop.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Users")
    users = cursor.fetchall()
    conn.close()

    users_json = []
    for user in users:
        temp_users = {
            "id" : user [0],
            "user_id" : user [1],
            "password" : user [2],
            "date_of_acount_creation" : user[3],
            "isApproved" : user[4],
            "block" : user [5],
            "name" : user [6],
            "address" : user [7],
            "email" : user[8],
            "phone_number": user [9],
            "pincode" : user [10]
        }
        users_json.append(temp_users)

    return users_json


def get_all_products():
    conn = sqlite3.connect("mymedicalshop.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Products")
    users = cursor.fetchall()
    conn.close()

    products_json = []
    for user in users:
        temp_products = {
            "id" : user [0],
            "product_id" : user [1],
            "product_name" : user [2],
            "price" : user[3],
            "stock" : user[4],
            "category" : user [5]
            
        }
        products_json.append(temp_products)

    return products_json


def get_all_order_details():
    conn = sqlite3.connect("mymedicalshop.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM OrderDetails")
    orders = cursor.fetchall()
    conn.close()

    orders_json = []
    for order in orders:
        temp_orders = {
            "id": order[0],
            "order_id": order[1],
            "product_id": order[2],
            "date_of_order_creation": order[3],
            "quantity": order[4],
            "product_price": order[5],
            "total_price": order[6],
            "product_name": order[7],
             "isApproved": order[8],
            "message": order[9],
            "user_name": order[10],
            "address": order[11],
            "category": order[12],
            "user_id": order[13],
            "email": order[14],
            "phone_number": order[15]
             
        }
        orders_json.append(temp_orders)

    return orders_json


def get_specific_user(userId):
    conn = sqlite3.connect("mymedicalshop.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Users WHERE user_id = ?", (userId,))
    
    user = cursor.fetchone()
    
    temp_user = {
            "id": user[0],
            "user_id": user[1],
            "password": user[2],
            "date_of_account_creation": user[3],
            "isApproved": user[4],
            "block": user[5],
            "name": user[6],
            "address": user[7],
            "email": user[8],
            "phone_number": user[9],
            "pincode": user[10]
        }
    
    conn.close()
    return temp_user


def get_specific_product(product_id):
    conn = sqlite3.connect("mymedicalshop.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Products WHERE product_id = ?", (product_id,))
    
    product = cursor.fetchone()
    
    temp_product = {
            "id": product[0],
            "product_id": product[1],
            "product_name": product[2],
            "price": product[3],
            "stock": product[4],
            "category": product[5]
        
        }
    
    conn.close()
    return temp_product        


def get_specific_order(order_id):   
    conn = sqlite3.connect("mymedicalshop.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM OrderDetails WHERE order_id = ?", (order_id,))
    
    order = cursor.fetchone()
    
    temp_orders = {
            "id": order[0],
            "order_id": order[1],
            "product_id": order[2],
            "date_of_order_creation": order[3],
            "quantity": order[4],
            "product_price": order[5],
            "total_price": order[6],
            "product_name": order[7],
            "isApproved": order[8],
            "message": order[9],
            "user_name": order[10],
            "address": order[11],
            "category": order[12],
            "user_id": order[13],
            "email": order[14],
            "phone_number": order[15]
             
        }
    
    conn.close()
    return temp_orders 
   
