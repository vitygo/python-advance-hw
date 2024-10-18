import sqlite3

connection = sqlite3.connect('dbex1.sqlite3')
cursor = connection.cursor()

def create_table_personal_expenses():
    query = '''
     CREATE TABLE IF NOT EXISTS personal_expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        purpuse VARCHAR(225) NOT NULL UNIQUE,
        amount REAL NOT NULL,
        time REAL NOT NULL
     );
     '''
    cursor.execute(query)

create_table_personal_expenses()

def add_expenses(purpuse: str, amount: float, time: float):
    query = '''
     INSERT INTO personal_expenses (purpuse, amount, time) VALUES (?, ?, ?);
     '''
    cursor.execute(query, [purpuse, amount, time])
    connection.commit()

add_expenses('food', 150.00, 12.20)