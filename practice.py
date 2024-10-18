# import sqlite3


# connection = sqlite3.connect("db.sqlite3")

# cursor = connection.cursor()

# def create_table_books():
#     query = '''
#     CREATE TABLE IF NOT EXISTS Books (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name VARCHAR(225) NOT NULL UNIQUE,
#         price REAL NOT NULL,
#         description TEXT
#     );
#     '''
#     cursor.execute(query)

# def add_book(name: str, price:float, description:str = None):
#     query = '''
#     INSERT INTO Books (name, description, price) VALUES (?,?,?);
#     '''
#     cursor.execute(query, [name, description, price])
#     connection.commit()

# # create_table_books()

# # add_book('Harry Potter5', 23.40, 'nice book')

# def get_all_books():
#     # query = "SELECT * FROM Books"
#     query = "SELECT name, price FROM Books;"
#     result = cursor.execute(query)
#     return result.fetchall()

# # print(get_all_books())

# def get_book(id):
#     query = '''
#     SELECT name, price FROM Books
#     WHERE id = ?
#     '''
#     result = cursor.execute(query, [id])
#     return result.fetchone()

# # print(get_book(3))

# def get_by_less_price(price:float):
#     query = '''
#     SELECT name, price FROM Books
#     WHERE id <= ?
#     '''
#     result = cursor.execute(query, [price])
#     return result.fetchall()

# print(get_by_less_price(100))

# def delete_book(id:int):
#     query = "DELETE FROM Books WHERE id = ?"
#     cursor.execute(query, [id])
#     connection.commit()

# delete_book(2)

#--------------------

import sqlite3

connection = sqlite3.connect('dbtest.sqlite3')

cursor = connection.cursor()

def create_table_employees():
    query = '''
     CREATE TABLE IF NOT EXISTS Employes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(225) NOT NULL UNIQUE,
        surename VARCHAR(225) NOT NULL UNIQUE,
        salary REAL NOT NULL
     );
     '''
    cursor.execute(query)

create_table_employees()

def add_employe(name:str, surename:str, salary:float):
    query = '''
     INSERT INTO IF NOT EXISTS Employes (name, surename, salary) VALUES (?,?,?);
     '''
    cursor.execute(query, [name, surename, salary])
    connection.commit()

add_employe('Bob', 'Bobow', 2500.50)

def get_all_employee():
    # query = "SELECT * FROM Books"
    query = "SELECT name, surename, salary FROM Employes;"
    result = cursor.execute(query)
    return result.fetchall()

print(get_all_employee())