import sqlite3

connection = sqlite3.connect('dbex3.sqlite3')
cursor = connection.cursor()

def create_table_personal_expenses():
    query = '''
     CREATE TABLE IF NOT EXISTS personal_expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        purpuse VARCHAR(225) NOT NULL UNIQUE,
        amount REAL NOT NULL,
        time REAL NOT NULL,
        type VARCHAR(10) NOT NULL CHECK(type IN ('income', 'expense'))
     );
     '''
    cursor.execute(query)


create_table_personal_expenses()

# Функція для додавання витрат або прибутків
def add_record(purpuse: str, amount: float, time: float, record_type: str):
    query = '''
     INSERT INTO personal_expenses (purpuse, amount, time, type) VALUES (?, ?, ?, ?);
     '''
    cursor.execute(query, [purpuse, amount, time, record_type])
    connection.commit()

# Додаємо витрати
add_record('food', 150.00, 12.20, 'expense')

# Додаємо прибутки
add_record('salary', 2000.00, 12.50, 'income')
