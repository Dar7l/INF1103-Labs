import math
from abc import ABC, abstractmethod

from supplier import Supplier


class Product(ABC):
    def __init__(
        self,
        product_id: str,
        name: str,
        price: float,
        stock: int,
        supplier: Supplier,
    ) -> None:
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
        self.__supplier: Supplier = supplier

    def get_product_id(self) -> str:
        return self.__product_id

    def get_supplier(self) -> Supplier:
        return self.__supplier

    def get_price(self) -> float:
        return self.__price

    def update_stock(self, quantity: int) -> None:
        if quantity < 0:
            raise ValueError("Stock cannot be negative.")

        self.__stock = quantity

    def display_information(self) -> None:
        print(
            f"{self.__product_id:<10} {self.__name:<25} "
            f"{self.__price:>10.2f} {self.__stock:>8}"
        )

    def to_dict(self) -> dict[str, str | int | float | dict[str, str]]:
        return {
            "id": self.__product_id,
            "name": self.__name,
            "price": self.__price,
            "stock": self.__stock,
            "supplier": self.__supplier.to_dict(),
        }

    @abstractmethod
    def get_fulfilment_info(self) -> str:
        pass