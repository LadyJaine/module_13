import sqlite3
connection = sqlite3.connect("database.db")
cursor = connection.cursor()

# for i in range(4):
#     cursor.execute('INSERT INTO Products(title,description,price) VALUES(?,?,?)',
#                    (f'Продукт{i + 1}',f'Описание {i + 1}',f'Стоимость{(i + 1) * 100}'))
#
# connection.commit()
# cursor.execute('DELETE FROM Products')
def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INT NOT NULL
    );
    ''')
    connection.commit()

def get_all_product():
    cursor.execute("SELECT * FROM Products")
    return cursor.fetchall()


connection.commit()
connection.close()