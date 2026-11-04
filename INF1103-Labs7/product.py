import math


class Product:
    def __init__(self, product_id, name, price, stock):
        if not product_id.strip() or not name.strip():
            raise ValueError("Product ID and name cannot be empty.")

        if not math.isfinite(price) or price < 0:
            raise ValueError("Price must be a finite, non-negative number.")

        if stock < 0:
            raise ValueError("Stock cannot be negative.")

        self.__product_id = product_id.strip().upper()
        self.__name = name.strip()
        self.__price = price
        self.__stock = stock

    def get_product_id(self):
        return self.__product_id

    def update_stock(self, quantity):
        if quantity < 0:
            raise ValueError("Stock cannot be negative.")

        self.__stock = quantity

    def display_information(self):
        print(
            f"{self.__product_id:<10} {self.__name:<25} "
            f"{self.__price:>10.2f} {self.__stock:>8}"
        )

    def to_dict(self):
        return {
            "id": self.__product_id,
            "name": self.__name,
            "price": self.__price,
            "stock": self.__stock
        }