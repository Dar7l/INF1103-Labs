import math

from product import Product
from can_be_shipped import CanBeShipped


class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, product_id, name, price, stock, weight):
        super().__init__(product_id, name, price, stock)

        if not math.isfinite(weight) or weight < 0:
            raise ValueError(
                "Weight must be a finite, non-negative number."
            )

        self.__weight = weight

    def display_information(self):
        super().display_information()

        print(f"  Weight: {self.__weight:.2f} kg")
        print(f"  {self.get_fulfilment_info()}")
        print(
            f"  Shipping cost: "
            f"${self.calculate_shipping_cost():.2f}"
        )

    def get_fulfilment_info(self):
        return "Requires physical shipping."

    def calculate_shipping_cost(self):
        return self.__weight * 5.0

    def to_dict(self):
        data = super().to_dict()

        data["type"] = "physical"
        data["weight"] = self.__weight

        return data