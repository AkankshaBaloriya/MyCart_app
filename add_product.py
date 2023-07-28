import sqlite3
import argparse
import sys
from Object_Models.products import AddProducts

    


connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()


# Step 3: Fetch categories from the "categories" table and present them as options to the user

# Fetch categories
cursor.execute('SELECT * FROM categories')
categories = cursor.fetchall()

# Display categories to the user
print("Categories: choose category id from here")
for category in categories:
    print(f"{category[0]}. {category[1]}")

# Step 4: Allow the user to choose a category for the product and save the product in the "product" table

product_name = input("Enter product name: ")
product_price = float(input("Enter product price: "))
chosen_category_id = int(input("Choose a category ID for the product: "))

detail=AddProducts(product_name, product_price, chosen_category_id )
name=detail.name
price=detail.price
category=detail.category_id


# Check if the chosen category ID is valid
valid_category_ids = [category[0] for category in categories]
if chosen_category_id not in valid_category_ids:
    print("Invalid category ID. Please choose a valid category.")
else:
    # Insert the product into the "product" table along with the chosen category ID
    cursor.execute('INSERT INTO product (name, price, category_id) VALUES (?, ?, ?)', (name, price,category))
    connection.commit()
    print("Product added successfully!")

# Close the connection
connection.close()


