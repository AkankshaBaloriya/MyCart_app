import sqlite3

connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()


# Create "product" table with a foreign key referencing "categories" table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS product (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        price REAL NOT NULL,
        category_id INTEGER NOT NULL,
        FOREIGN KEY (category_id) REFERENCES categories(id)
    )
''')


# Create "categories" table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS categories (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        product_id INTEGER NOT NULL,
        FOREIGN KEY (product_id) REFERENCES product(id)   
    )
''')

# created "cart" table in sqlite3

cursor.execute('''
        CREATE TABLE IF NOT EXISTS cart (
            id INTEGER PRIMARY KEY,
            product_id INTEGER NOT NULL,
            quantity INTEGER NOT NULL,
            product_name TEXT NOT NULL,
            price REAL NOT NULL,
            category_id INTEGER NOT NULL,
            user_name TEXT NOT NULL,  
            FOREIGN KEY (product_id) REFERENCES product(id),
            FOREIGN KEY (category_id) REFERENCES categories(id)
        )
    ''')

# created "buy_product" table in sqlite3

cursor.execute('''
               CREATE TABLE IF NOT EXISTS buy_product (
                   id INTEGET PRIMAY KEY,
                   product_name TEXT NOT NULL,
                   product_price REAL NOT NULL,
                   quantity REAL NOT NULL,
                   user_name TEXT NOT NULL,
                   FOREIGN KEY (id) REFERENCES cart(id)
               )
               ''')



