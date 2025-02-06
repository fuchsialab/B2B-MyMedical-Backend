import sqlite3
import uuid
from datetime import date

def create_User( name, password, address, email, phone_number, pincode):

    conn = sqlite3.connect("mymedicalshop.db")
    cursor = conn.cursor()
    dateofaccountcreation = date.today()
    userid = str(uuid.uuid4())
    cursor.execute('''

        INSERT INTO Users(name, password, date_of_account_creation, isApproved, block, email, address, pincode, phone_number, user_id)
            VALUES(?,?,?,?,?,?,?,?,?,? )
                   
        ''',(name, password, dateofaccountcreation, 0,0, email, address, pincode, phone_number, userid)

    )
    conn.commit()
    conn.close()
    return userid

def create_Product(category, stock, price, product_name):

    conn = sqlite3.connect("mymedicalshop.db")
    cursor = conn.cursor()
    product_id = str(uuid.uuid4())
    cursor.execute('''

        INSERT INTO Products(category, stock, price, product_name, product_id)
            VALUES(?,?,?,?,?)
                   
        ''',(category, stock, price, product_name, product_id)

    )
    conn.commit()
    conn.close()
    return product_id

def create_order_details(user_name, quantity, product_price, total_price, product_name, message, category, user_id, email, address, phone_number, product_id):

    conn = sqlite3.connect("mymedicalshop.db")
    cursor = conn.cursor()
    date_of_order_creation = date.today()
    order_id = str(uuid.uuid4())
    isApproved = str(0)
    cursor.execute('''

        INSERT INTO OrderDetails(date_of_order_creation, user_name, quantity, product_price, total_price, product_name, message, category, user_id, email, address, phone_number, order_id, product_id, isApproved)
            VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
                   
        ''',(date_of_order_creation, user_name, quantity, product_price, total_price, product_name, message, category, user_id, email, address, phone_number, order_id, product_id, isApproved)

    )
    conn.commit()
    conn.close()
    return order_id


def SalesHistory(user_id, product_id, quantity, remaining_stock, product_price, product_name, user_name):
    conn = sqlite3.connect("mymedicalshop.db")
    cursor = conn.cursor()
    sale_id = str(uuid.uuid4())
    date_of_sale = date.today()
    cursor.execute('''

        INSERT INTO SaleHistory(sale_id, user_id, product_id, quantity, remaining_stock, product_price, date_of_sale, product_name, user_name)
            VALUES(?,?,?,?,?,?,?,?,?)
                   
        ''',(sale_id, user_id, product_id, quantity, remaining_stock, product_price, date_of_sale, product_name, user_name)

    )
    conn.commit()
    conn.close()
    return sale_id

def User_Stock(user_id, product_id, stock, product_price, product_name, user_name, category):
    conn = sqlite3.connect("mymedicalshop.db")
    cursor = conn.cursor()    
    cursor.execute('''
                   
                   INSERT INTO UserStock(user_id, product_id, stock, product_price, product_name, user_name, category)
                    VALUES(?,?,?,?,?,?,?)
                     
                     ''',(user_id, product_id, stock, product_price, product_name, user_name, category)


    )
    conn.commit()
    conn.close()
    return user_id

    