from product import Product
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from can_be_shipped import CanBeShipped
from inventory import Inventory


def main():
    laptop = PhysicalProduct(
        "P100", "Test Laptop", 1200.0, 15, 2.0
    )

    mouse = PhysicalProduct(
        "P101", "Test Mouse", 25.5, 40, 0.2
    )

    ebook = DigitalProduct(
        "D100", "Test E-book", 9.9, 100, 25.0
    )

    print("PHYSICAL PRODUCT")
    laptop.display_information()

    print("\nDIGITAL PRODUCT")
    ebook.display_information()

    assert laptop.calculate_shipping_cost() == 10.0
    assert mouse.calculate_shipping_cost() == 1.0
    print("\nPASS: shipping costs at two weights")

    assert isinstance(laptop, CanBeShipped)
    assert not isinstance(ebook, CanBeShipped)
    assert not hasattr(ebook, "calculate_shipping_cost")
    print("PASS: shipping applies only to physical products")

    assert laptop.get_fulfilment_info() == (
        "Requires physical shipping."
    )
    assert ebook.get_fulfilment_info() == (
        "Delivered digitally by download."
    )
    print("PASS: both fulfilment methods work")

    try:
        Product("X001", "Generic Product", 1.0, 1)

    except TypeError as error:
        print(f"PASS: abstract Product rejected: {error}")

    else:
        raise AssertionError(
            "Product should not be directly instantiable."
        )

    inventory = Inventory()

    assert inventory.add_product(laptop)
    assert inventory.add_product(ebook)
    assert not inventory.add_product(laptop)

    assert inventory.search_product("D100") is ebook
    assert inventory.update_stock("P100", 50)
    assert laptop.to_dict()["stock"] == 50

    print("PASS: inventory manages both product types")


if __name__ == "__main__":
    main()