import sqlite3


def delete_User(user_id):
    conn = sqlite3.connect("mymedicalshop.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Users WHERE user_id = ?", (user_id,))
    conn.commit()
    conn.close()
    return user_id