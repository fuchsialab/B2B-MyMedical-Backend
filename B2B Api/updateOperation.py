import sqlite3


def update_User(user_id, update_list):
    conn = sqlite3.connect("mymedicalshop.db")
    cursor = conn.cursor()

    for key, value in update_list.items():
        if   key == 'name':
            cursor.execute("UPDATE Users SET name = ? WHERE user_id = ?", (value, user_id))
        elif key == 'password':
            cursor.execute("UPDATE Users SET password = ? WHERE user_id = ?", (value, user_id))        
        elif key == 'address':
            cursor.execute("UPDATE Users SET address = ? WHERE user_id = ?", (value, user_id))
        elif key == 'email':
            cursor.execute("UPDATE Users SET email = ? WHERE user_id = ?", (value, user_id))
        elif key == 'phone_number':
            cursor.execute("UPDATE Users SET phone_number = ? WHERE user_id = ?", (value, user_id))
        elif key == 'pincode':
            cursor.execute("UPDATE Users SET pincode = ? WHERE user_id = ?", (value, user_id))
        elif key == 'isApproved':
            cursor.execute("UPDATE Users SET isApproved = ? WHERE user_id = ?", (value, user_id))
        elif key == 'block':
            cursor.execute("UPDATE Users SET block = ? WHERE user_id = ?", (value, user_id))           

           
    conn.commit()
    conn.close()
    return user_id




def update_Order(order_id, update_list):
    conn = sqlite3.connect("mymedicalshop.db")
    cursor = conn.cursor()

    for key, value in update_list.items():
        if key == 'total_price':
            cursor.execute("UPDATE OrderDetails  SET total_price = ? WHERE order_id = ?", (value, order_id))
        elif key == 'isApproved':
            cursor.execute("UPDATE OrderDetails  SET isApproved = ? WHERE order_id = ?", (value, order_id))
        elif key == 'message':
            cursor.execute("UPDATE OrderDetails  SET message = ? WHERE order_id = ?", (value, order_id))

    conn.commit()
    conn.close()
    return order_id

        
def updateProductQuantity(product_id, update_list):
    conn = sqlite3.connect("mymedicalshop.db")
    cursor = conn.cursor()

    for key, value in update_list.items():

        if key == 'stock':
            cursor.execute("UPDATE Products SET stock = stock - ? WHERE product_id = ?", (value, product_id))


    conn.commit()
    conn.close()
    return product_id
       

    
