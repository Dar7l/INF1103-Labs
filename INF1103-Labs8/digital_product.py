import math

from product import Product
from supplier import Supplier


class DigitalProduct(Product):
    def __init__(
        self,
        product_id: str,
        name: str,
        price: float,
        stock: int,
        download_size: float,
        supplier: Supplier,
    ) -> None:
        super().__init__(product_id, name, price, stock, supplier)

        if not math.isfinite(download_size) or download_size < 0:
            raise ValueError(
                "Download size must be a finite, "
                "non-negative number."
            )

        self.__download_size: float = download_size

    def display_information(self) -> None:
        super().display_information()

        print(f"  Download size: {self.__download_size:.2f} MB")
        print(f"  {self.get_fulfilment_info()}")

    def get_fulfilment_info(self) -> str:
        return "Delivered digitally by download."

    def to_dict(self) -> dict[str, str | int | float | dict[str, str]]:
        data = super().to_dict()
        data["type"] = "digital"
        data["download_size"] = self.__download_size
        return data