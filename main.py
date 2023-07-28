import argparse
import sqlite3
import argparse
import os


# *******************show list of all Product************************
def Product_list():
   
	connection = sqlite3.connect('my_database.db')
	cursor = connection.cursor()
	print("      id ","name   ","price ", "category_id ")
	print("______________________________________")
	data=cursor.execute("SELECT * from Product")

	for i in data:
		print("     ",i, "      ")
	print("")    

	cursor.close()

#  *******************show list of all Category***********************

def Category_list():
    # Implement your addProduct logic he
		connection = sqlite3.connect('my_database.db')
		cursor = connection.cursor()
		print("       id  ","  name")
		print("______________________________________")
		data=cursor.execute("SELECT * from categories")

		for i in data:
			print("     ",i, "      ")
		print("")    

		cursor.close()

#  *******************get products of any speciafic category only***********************
def Category_item():
    
        connection = sqlite3.connect('my_database.db')
        cursor = connection.cursor()
        print("       id  ","  name")
        print("______________________________________")
        data=cursor.execute("SELECT * from categories")
		
        for i in data:
            print("     ",i, "      ")
        cursor.close()        
        def get_products_by_category(category_name):
            # Connect to the SQLite database
            connection = sqlite3.connect('my_database.db')
            cursor = connection.cursor()



            # Find the corresponding category ID based on the given category name
            cursor.execute("SELECT id FROM categories WHERE name = ?", (category_name,))
            category_id = cursor.fetchone()

            if category_id is None:
                print(f"No Category named '{category_name}' found.")
            else:
                category_id = category_id[0]

                # Use a SQL query with a JOIN statement to retrieve all products under the particular category
                cursor.execute("SELECT * FROM product WHERE category_id = ?", (category_id,))
                products_data = cursor.fetchall()

                # Close the connection
                cursor.close()

                # Display the products to the user
                if len(products_data) > 0:
                    print(f"p_id","    name","             price","c_id")
                    print("______________________________________________")
                    for product in products_data:
                        print(product)	
                else:
                    print(f"No products found for category '{category_name}'.")

        if __name__ == '__main__':
            category_name = input("Enter the name of the category to show products: ")
            print(" All Products under",{category_name})
            get_products_by_category(category_name)


#***********************************Add products in cart********************************** 

def Add_in_cart():
    connection = sqlite3.connect('my_database.db')
    cursor = connection.cursor()
    print("      id ","name   ","price ", "category_id ")
    print("______________________________________")

    data=cursor.execute("SELECT * from Product")
    for i in data:
        print("     ",i, "      ")
        
        
    def create_cart_table():
        connection = sqlite3.connect('my_database.db')
        # cursor = connection.cursor() 
        connection.commit()
        connection.close()

    # Step 2: Implement the function to add products to the cart
    def add_to_cart(product_id, quantity, user_name):
        connection = sqlite3.connect('my_database.db')
        cursor = connection.cursor()

        # Fetch product details from the "products" table
        cursor.execute('SELECT name, price, category_id FROM product WHERE id = ?', (product_id,))
        product_details = cursor.fetchone()

        if product_details:
            product_name, price, category_id = product_details

            # Insert the product into the "cart" table along with the provided quantity and user ID
            cursor.execute('INSERT INTO cart (product_id, quantity, product_name, price, category_id, user_name) VALUES (?, ?, ?, ?, ?, ?)',
                        (product_id, quantity, product_name, price, category_id, user_name))
            connection.commit()
            print("Product added to the cart of",user_name," successfully!")
        else:
            print("Product with the given ID not found in the products table.")

        connection.close()
        
    more=str(input("do you wanna add product Y/q"))
    while more!= "q":
        # more=str(input("do you wanna add more products Y/q"))

        if __name__ == '__main__':
            create_cart_table()
            while more!= "q":
                product_id = int(input("Enter the product ID you want to add to the cart: "))
                quantity = int(input("Enter the quantity of the product: "))
                user_name = str(input("Enter the user name: "))
                add_to_cart(product_id, quantity, user_name)
                more=str(input("Do you want more Y/q"))
                while more=="q":
                    print("your product is added, please come back to shop!")
                    break

# *********************** remove products from cart********************************
                
def Remove_cart_product():
    connection=sqlite3.connect("my_database.db")
    cursor=connection.cursor()

    remove=input("Do you wanna remove any item (y/n)")
    while remove!="n":
        cart_item=cursor.execute("SELECT * FROM cart")
        print("c_p_id, p_id, quantity, price, user_name")
        print("_______________________________________________")
        for i in cart_item:
            print(i)
        print("your cart items are given above")    
        aa=int(input("Enter the Cart product id(c_p_id) which you wish to remove!"))    
        cursor.execute("DELETE FROM cart WHERE id = ?", (aa,))
        print("your item is Removed")
        
        remov=input("Do you wanna remove more products (y/n)")
        
        while remov=="n":
            print("thanks")
            break

        connection.commit()
    connection.close()     
    
    # *********************buy product from cart*****************************************
    
def Buy_product_from_cart():
    connection = sqlite3.connect("my_database.db")
    cursor = connection.cursor()

    buy = input("Do you wanna buy products from cart (y/n): ")

    while buy != "n":
        print("These are the products in cart:")
        cart = cursor.execute("SELECT * FROM cart")
        print("cp_id ,p_id,quantity,name,price,c_id,user_name ")
        for i in cart:
            print(i)

        buy = int(input("Enter the ID of the product (cp_id) from cart to buy "))


        cursor.execute("SELECT product_name, price, user_name, quantity FROM cart WHERE id = ?", (buy,))
        buy_product = cursor.fetchone()

        if buy_product:
            product_name, price, user_name, quantity = buy_product

            cursor.execute("INSERT INTO buy_product (product_name, product_price, user_name, quantity) VALUES (?, ?, ?, ?)", (product_name, price, user_name, quantity))
            cursor.execute("DELETE FROM cart WHERE id = ?", (buy,))
            connection.commit()

            print(f"Product '{product_name}' successfully bought and added to the 'buy_product' table.")
        else:
            print("No product found with the given ID in the cart.")

        buy = input("Do you wanna buy more products from cart(y/n): ")

    connection.close()


def Bill_generater():
    def get_user_products(user_name):
        connection = sqlite3.connect('my_database.db')
        cursor = connection.cursor()
        cursor.execute("SELECT product_name, product_price, quantity FROM buy_product WHERE user_name = ?", (user_name,))
        user_products = cursor.fetchall()
        connection.close()
        return user_products

    def calculate_total_price(products):
        total_price = sum(product[1] * product[2] for product in products)
        return total_price

    def apply_discount(total_price):
        if total_price > 10000:
            return total_price - 500
        else:
            return total_price

    user_name = input("Enter the username to generate bill: ")

    user_products = get_user_products(user_name)
    if user_products:
        print("\nProducts for user:", user_name)
        for product in user_products:
            print("Product Name:", product[0])
            print("Price:", product[1])
            print("Quantity:", product[2])
            print("--------------")

        total_price = calculate_total_price(user_products)
        final_price = apply_discount(total_price)

        print("\nFinal Billing Statement:")
        print("User Name:", user_name)
        print("Total Price: Rs.", total_price)
        if final_price < total_price:
            print("Discount Applied: Rs. 500")
        print("Final Amount to Pay: Rs.", final_price)
        
        connection = sqlite3.connect('my_database.db')
        cursor = connection.cursor()
        cursor.execute("DELETE FROM buy_product WHERE user_name = ?", (user_name,))
        connection.commit()
        connection.close()
        
        bills_folder = "bills"
        if not os.path.exists(bills_folder):
            os.makedirs(bills_folder)

        # Creating the text file bill
        bill_file_path = os.path.join(bills_folder, f"{user_name}_bill.txt")
        with open(bill_file_path, "w") as file:
            file.write("Billing Details for User: " + user_name + "\n")
            file.write("------------------------------\n")
            for product in user_products:
                file.write("Product Name: " + product[0] + "\n")
                file.write("Price: Rs. " + str(product[1]) + "\n")
                file.write("Quantity: " + str(product[2]) + "\n")
                file.write("--------------\n")
            
            file.write("\nFinal Billing Statement:\n")
            file.write("Total Price: Rs. " + str(total_price) + "\n")
            if final_price < total_price:
                file.write("Discount Applied: Rs. 500\n")
            file.write("Final Amount to Pay: Rs. " + str(final_price) + "\n")

        print("Billing details saved to", bill_file_path)
            
    else:
        print("No products found for the user:", user_name)
        
    
    
    
    


#************************* CREATEED ALL THE UTILITIES  USING argparse ***********************



if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    subparsers = parser.add_subparsers(title='subcommands', dest='subcommand')

    # Subparser for Category_list command
    parser_add_category = subparsers.add_parser('Category_list', help='Add a new category')
    

    # Subparser for Product_list command
    parser_add_product = subparsers.add_parser('Product_list', help='Add a new product')
    
    # Subparser to get products of any particular categories
    parser_add_product = subparsers.add_parser('Category_item', help='Add a new product')
    
    parser_add_product = subparsers.add_parser('Add_in_cart', help='Add products in cart')
    
    parser_add_product = subparsers.add_parser('Remove_cart_product', help='Remove the product from Cart')

    parser_add_product = subparsers.add_parser('Buy_product_from_cart', help='Buy product from cart')
    
    parser_add_product = subparsers.add_parser('Bill_generater', help='generate_bill')

    args = parser.parse_args()

    if args.subcommand == 'Category_list':
        Category_list()
        
    elif args.subcommand == 'Product_list':
        Product_list()
    
    elif args.subcommand=="Category_item":
        Category_item()
        
    elif args.subcommand == 'Add_in_cart':
        Add_in_cart()        
        
    elif args.subcommand=="Remove_cart_product":
        Remove_cart_product()
        
    elif args.subcommand=="Buy_product_from_cart":
        Buy_product_from_cart()    
        
    elif args.subcommand=="Bill_generater":
        Bill_generater()        
         