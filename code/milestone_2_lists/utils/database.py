from typing import List, Dict, Union
from .database_connection import DatabaseConnection

"""
Concerned with storing and retrieving books from a database.
"""

Book = Dict(str, Union(str, int))

def create_book_table() -> None:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('CREATE TABLE IF NOT EXISTS books(name text primary key, author text, read integer)')

def add_book(name: str,author: str) -> None:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('INSERT INTO books VALUES(?,?,0)',(name, author))


def get_all_books() -> List[Book]:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM books')
        books = [{'name': row[0], 'author': row[1], 'read':row[2]} for row in cursor.fetchall()]
    return books

# def _save_all_books(books):
#     with open(books_file, 'w') as file:
#         json.dump(books, file)

def view_book(name):
    books = get_all_books()
    return [book for book in books if book['name']==name]

def mark_read(name: str) -> None:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('UPDATE books SET read=1 WHERE name=?',(name,))



def delete_book(name: str) -> None:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('DELETE FROM books WHERE name=?',(name,))


# """
# Concerned with storing and retrieving books from a json file.
# [
#     {
#         'name': 'Clean Code',
#         'author': 'Robert',
#         'read': True
#     }
# ]
# """
# import json
# books_file = 'books.json'

# def create_book_table():
#     with open(books_file, 'w') as file:
#         json.dump([], file)

# def add_book(name,author):
#     books = get_all_books()
#     books.append({'name': name, 'author': author, 'read': False})
#     _save_all_books(books)

# def get_all_books():
#     with open(books_file, 'r') as file:
#         return json.load(file)

# def _save_all_books(books):
#     with open(books_file, 'w') as file:
#         json.dump(books, file)

# def view_book(name):
#     books = get_all_books()
#     return [book for book in books if book['name']==name]

# def mark_read(name):
#     books = get_all_books()
#     for book in books:
#         if book['name'] == name:
#             book['read'] = True
#     _save_all_books(books)


# def delete_book(name):
#     books = get_all_books()
#     books = [book for book in books if book['name'] != name]
#     _save_all_books(books)
            


# """
# Concerned with storing and retrieving books from a csv file.
# name,author,read\n
# name,author,read\n
# name,author,read\n
# """
# books_file = 'books.txt'

# def create_book_table():
#     with open(books_file, 'w'):
#         pass  # Just to make sure the file is there

# def add_book(name,author):
#     with open(books_file,'a') as file:
#         file.write(f'{name},{author},0\n')

# def get_all_books():
#     with open(books_file, 'r') as file:
#         lines = [line.strip().split(',') for line in file.readlines()]
#     return [
#         {'name': line[0], 'author': line[1], 'read': line[2]}
#         for line in lines
#     ]


# def view_book(name):
#     return [book for book in books if book['name']==name]

# def mark_read(name):
#     books = get_all_books()
#     for book in books:
#         if book['name']==name:
#             book['read']='1'
#     _save_all_books(books)

# def _save_all_books(books):
#     with open(books_file, 'w') as file:
#         for book in books:
#             file.write(f"{book['name']},{book['author']},{book['read']}\n")

# def delete_book(name):
#     books = get_all_books()
#     books = [book for book in books if book['name'] != name]
#     _save_all_books(books)
            

# Using lists   
# books = []

# def add_book(name,author):
#     books.append({'name': name,'author': author, 'read': False})

# def get_all_books():
#     return books

# def view_book(name):
#     return [book for book in books if book['name']==name]

# def mark_read(name):
#    for book in books:
#        if book['name']==name:
#            book['read']=True

# def delete_book(name):
#     global books
#     books = [book for book in books if book['name']!=name]

    