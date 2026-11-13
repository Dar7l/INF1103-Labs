import math

from can_be_shipped import CanBeShipped
from product import Product
from supplier import Supplier


class PhysicalProduct(Product, CanBeShipped):
    def __init__(
        self,
        product_id: str,
        name: str,
        price: float,
        stock: int,
        weight: float,
        supplier: Supplier,
    ) -> None:
        super().__init__(product_id, name, price, stock, supplier)

        if not math.isfinite(weight) or weight < 0:
            raise ValueError(
                "Weight must be a finite, non-negative number."
            )

        self.__weight: float = weight

    def display_information(self) -> None:
        super().display_information()

        print(f"  Weight: {self.__weight:.2f} kg")
        print(f"  {self.get_fulfilment_info()}")
        print(f"  Shipping cost: ${self.calculate_shipping_cost():.2f}")

    def get_fulfilment_info(self) -> str:
        return "Requires physical shipping."

    def calculate_shipping_cost(self) -> float:
        return self.__weight * 5.0

    def to_dict(self) -> dict[str, str | int | float | dict[str, str]]:
        data = super().to_dict()
        data["type"] = "physical"
        data["weight"] = self.__weight
        return data