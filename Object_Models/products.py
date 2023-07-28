class AddProducts:
    def __init__(self, name, price, category_id):
        self.name = name
        self.price = price
        self.category_id=category_id

    def __str__(self):
        return f"AddProdcts: name={self.name}, price={self.price}, category_id={self.category_id}"