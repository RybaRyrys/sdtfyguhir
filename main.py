import sqlite3


def create_table():
    conn = sqlite3.connect('newdb.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS doll
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT,
                 brand TEXT,
                 company TEXT,
                 price REAL)''')
    conn.commit()
    conn.close()


def select_doll():
    conn = sqlite3.connect('newdb.db')
    c = conn.cursor()

    c.execute("SELECT * FROM doll")
    doll = c.fetchall()

    for doll1 in doll:
        print(doll1)

    conn.close()


def add_doll(name, brand, company, price):
    conn = sqlite3.connect('newdb.db')
    c = conn.cursor()

    c.execute("INSERT INTO doll (name, brand, company, price) VALUES (?, ?, ?, ?)",
              (name, brand, company, price))

    conn.commit()
    conn.close()


def update_price(name, new_price):
    conn = sqlite3.connect('newdb.db')
    c = conn.cursor()

    c.execute("UPDATE doll SET price = ? WHERE name = ?", (new_price, name))

    conn.commit()
    conn.close()


def delete_doll(name):
    conn = sqlite3.connect('newdb.db')
    c = conn.cursor()

    c.execute("DELETE FROM doll WHERE name = ?", name)

    conn.commit()
    conn.close()



def find_doll(name):
    conn = sqlite3.connect('newdb.db')
    c = conn.cursor()

    c.execute("SELECT * FROM doll WHERE name = ?", name)
    doll1 = c.fetchone()

    if doll1:
        print(doll1)
    else:
        print("Кукла не найдена")

    conn.close()


create_table()
while True:
    print("1 - Просмотреть всех кукол")
    print("2 - Добавить куклу")
    print("3 - Изменить цену куклы")
    print("4 - Удалить куклу")
    print("5 - Найти куклу")
    print("0 - Выход")

    choice = input("Введите код команды: ")

    if choice == "1":
        select_doll()
    elif choice == "2":
        name = input("Введите имя куклы: ")
        brand = input("Введите имя бренда: ")
        company = input("Введите имя компании: ")
        price = float(input("Введите цену куклы: "))
        add_doll(name, brand, company, price)
    elif choice == "3":
        name = input("Введите имя куклы: ")
        new_price = float(input("Введите новую цену куклы: "))
        update_price(name, new_price)
    elif choice == "4":
        name = input("Введите имя куклы: ")
        delete_doll(name)
    elif choice == "5":
        name = input("Введите имя куклы: ")
        find_doll(name)
    elif choice == "0":
        break
    else:
        print("Неверная команда")