from digital_product import DigitalProduct
from inventory import Inventory
from physical_product import PhysicalProduct
from product import Product
from supplier import Supplier


def show_product_details(product: Product) -> None:
    product.display_information()
    print("Fulfilment result:", product.get_fulfilment_info())


def main() -> None:
    supplier = Supplier("S001", "Test Supplier", "test@example.com")
    laptop = PhysicalProduct("P100", "Test Laptop", 1200.0, 15, 2.0, supplier)
    ebook = DigitalProduct("D100", "Test E-book", 9.90, 20, 25.0, supplier)

    inventory = Inventory()
    inventory.add_product(laptop)
    inventory.add_product(ebook)

    for product in inventory.get_products():
        product_id = product.get_product_id()
        print(f"\nTesting {product_id}")

        updated = inventory.update_stock(product_id, 30)
        assert updated
        assert product.to_dict()["stock"] == 30
        print("Stock successfully set to 30.")

        show_product_details(product)


if __name__ == "__main__":
    main()