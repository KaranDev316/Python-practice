import sqlite3
titles = [
    (1, "The Pragmatic Programmer"),
    (2, "Clean Code"),
    (3, "Fluent Python")
]
with sqlite3.connect("library.db") as connection:
    cursor = connection.cursor()
    cursor.execute(""" 
       CREATE TABLE IF NOT EXISTS temperature (
         id INTEGER,
         title TEXT
        )
    """)
for  title in titles:
    cursor.execute("INSERT INTO temperature VALUES (?,?)", (title[0], title[1]))
