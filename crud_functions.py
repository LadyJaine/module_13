import sqlite3


def initiate_db():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INT NOT NULL
    );
    ''')
    # for i in range(4):
    #     cursor.execute('INSERT INTO Products(title,description,price) VALUES(?,?,?)',
    #                    (f'Продукт{i + 1}', f'Описание {i + 1}', f'Стоимость{(i + 1) * 100}'))
    connection.commit()
    cursor.close()
    connection.close()


def get_all_product():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Products")
    cur_f = cursor.fetchall()
    cursor.close()
    connection.close()
    return cur_f



if __name__ == '__main__':
    print(get_all_product())
