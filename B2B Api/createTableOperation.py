import sqlite3

def createTables():
    conn = sqlite3.connect("mymedicalshop.db")
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id VARCHAR(255),
        password VARCHAR(255),
        date_of_account_creation VARCHAR(255),
        isApproved BOOLEAN,
        block BOOLEAN,
        name VARCHAR(255),
        address VARCHAR(255),
        email VARCHAR(255),
        phone_number VARCHAR(255),
        pincode VARCHAR(255)
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_id VARCHAR(255),
        product_name VARCHAR(255),
        price FLOAT,
        stock INTEGER,
        category VARCHAR(255)
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS OrderDetails (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        order_id VARCHAR(255),
        product_id VARCHAR(255),
        date_of_order_creation VARCHAR(255),
        quantity INTEGER,
        product_price FLOAT,
        total_price FLOAT,
        product_name VARCHAR(255),
        isApproved VARCHAR(255),
        message VARCHAR(255),
        user_name VARCHAR(255),
        address VARCHAR(255),
        category VARCHAR(255),
        user_id VARCHAR(255),
        email VARCHAR(255),
        phone_number VARCHAR(255)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS SaleHistory (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        sale_id VARCHAR(255),
        product_id VARCHAR(255),
        quantity INTEGER,
        remaining_stock INTEGER,
        product_price FLOAT,
        date_of_sale VARCHAR(255),
        product_name VARCHAR(255),
        user_name VARCHAR(255),
        user_id VARCHAR(255)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS UserStock (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_id VARCHAR(255),
        stock INTEGER,
        category VARCHAR(255),
        product_price FLOAT,
        product_name VARCHAR(255),
        user_name VARCHAR(255),
        user_id VARCHAR(255)
    )
    ''')

    conn.commit()
    conn.close()
