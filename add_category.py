import sqlite3
from Object_Models.category import AddCategories

# Step 1: Set up SQLite database with two tables - "product" and "categories"
connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

names = input("Enter the name of your Category: ")
print("Added")
detail = AddCategories(names)
name = detail.name

print(name)
cursor.execute("insert into categories (name) VALUES (?)", (name, ))

# Commit changes to the database
connection.commit()