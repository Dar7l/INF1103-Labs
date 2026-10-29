class Inventory:
    def __init__(self):
        self.__products = []

    def add_product(self, product):
        if self.search_product(product.get_product_id()) is not None:
            return False

        self.__products.append(product)
        return True

    def search_product(self, product_id):
        product_id = product_id.strip().upper()

        for product in self.__products:
            if product.get_product_id() == product_id:
                return product

        return None

    def update_stock(self, product_id, quantity):
        product = self.search_product(product_id)

        if product is None:
            return False

        product.update_stock(quantity)
        return True

    def display_all(self):
        if not self.__products:
            print("No products in inventory.")
            return

        print(
            f"{'ID':<10} {'Name':<25} "
            f"{'Price':>10} {'Stock':>8}"
        )
        print("-" * 56)

        for product in self.__products:
            product.display_information()

    def get_products(self):
        return self.__products.copy()