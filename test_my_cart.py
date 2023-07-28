import unittest
import io
import sys
from main import Add_in_cart, Remove_cart_product, Buy_product_from_cart, Bill_generater

class TestMyApp(unittest.TestCase):
    def test_add_in_cart(self):
        # Test case for Add_in_cart function
        expected_output = "Product added to the cart of <username> successfully!"
        
        captured_output = io.StringIO()
        sys.stdout = captured_output

        # Call the function that adds a product to the cart
        # You may need to provide appropriate input for this test case
        Add_in_cart()

        # Reset the standard output
        sys.stdout = sys.__stdout__

        # Compare the captured output with the expected output
        self.assertEqual(captured_output.getvalue().strip(), expected_output)

    def test_remove_cart_product(self):
        # Test case for Remove_cart_product function
        expected_output = "your item is Removed"
        
        captured_output = io.StringIO()
        sys.stdout = captured_output

        # Call the function that removes a product from the cart
        # You may need to provide appropriate input for this test case
        Remove_cart_product()

        # Reset the standard output
        sys.stdout = sys.__stdout__

        # Compare the captured output with the expected output
        self.assertEqual(captured_output.getvalue().strip(), expected_output)

    def test_buy_product_from_cart(self):
        # Test case for Buy_product_from_cart function
        expected_output = "Product 'Product A' successfully bought and added to the 'buy_product' table."
        
        captured_output = io.StringIO()
        sys.stdout = captured_output

        # Call the function that buys a product from the cart
        # You may need to provide appropriate input for this test case
        Buy_product_from_cart()

        # Reset the standard output
        sys.stdout = sys.__stdout__

        # Compare the captured output with the expected output
        self.assertEqual(captured_output.getvalue().strip(), expected_output)

    def test_bill_generater(self):
        expected_output = "Final Billing Statement:\nUser"


