import json
from pathlib import Path

from digital_product import DigitalProduct
from inventory import Inventory
from physical_product import PhysicalProduct
from supplier import Supplier


FILENAME = Path(__file__).resolve().parent / "inventory.json"


def load_inventory() -> Inventory:
    inventory = Inventory()

    try:
        with open(FILENAME, "r", encoding="utf-8") as file:
            records = json.load(file)

    except FileNotFoundError:
        print("Inventory file not found. Starting empty.")
        return inventory

    if not isinstance(records, list):
        raise ValueError("Inventory data must be a list.")

    for record in records:
        product_type = record["type"]
        product_id = record["id"]
        name = record["name"]
        price = float(record["price"])
        stock = int(record["stock"])

        supplier_data = record.get("supplier")
        if supplier_data is None:
            supplier = Supplier("LEGACY", "Unknown supplier", "")
        else:
            supplier = Supplier(
                supplier_data["supplier_id"],
                supplier_data["name"],
                supplier_data["contact_email"],
            )

        if product_type == "physical":
            product = PhysicalProduct(
                product_id,
                name,
                price,
                stock,
                float(record["weight"]),
                supplier=supplier,
            )

        elif product_type == "digital":
            product = DigitalProduct(
                product_id,
                name,
                price,
                stock,
                float(record["download_size"]),
                supplier=supplier,
            )

        else:
            raise ValueError(f"Unknown product type: {product_type}")

        if not inventory.add_product(product):
            raise ValueError(f"Duplicate product ID: {product_id}")

    print("Inventory loaded successfully.")
    return inventory


def save_inventory(inventory: Inventory) -> None:
    records = []

    for product in inventory.get_products():
        records.append(product.to_dict())

    with open(FILENAME, "w", encoding="utf-8") as file:
        json.dump(records, file, indent=4)

    print("Inventory saved successfully.")


def display_menu() -> None:
    print("\n=== Inventory Management System ===")
    print("1. Display all products")
    print("2. Add a product")
    print("3. Update stock")
    print("4. Search for a product")
    print("5. Save inventory")
    print("6. Exit")


def add_product_from_input(inventory: Inventory) -> None:
    print("\nProduct types:")
    print("1. Physical product")
    print("2. Digital product")

    product_type = input("Choose product type: ").strip()

    if product_type not in ("1", "2"):
        print("Invalid product type.")
        return

    product_id = input("Product ID: ")
    name = input("Product name: ")
    price = float(input("Price: "))
    stock = int(input("Stock quantity: "))

    supplier = Supplier(
        input("Supplier ID: ").strip(),
        input("Supplier name: ").strip(),
        input("Supplier contact email: ").strip(),
    )

    if product_type == "1":
        weight = float(input("Weight in kg: "))

        product = PhysicalProduct(
            product_id, name, price, stock, weight, supplier=supplier
        )

    else:
        download_size = float(input("Download size in MB: "))

        product = DigitalProduct(
            product_id, name, price, stock, download_size, supplier=supplier
        )

    if inventory.add_product(product):
        print("Product added successfully.")
    else:
        print("A product with that ID already exists.")


def main() -> None:
    try:
        inventory = load_inventory()

    except (OSError, ValueError, KeyError, TypeError) as error:
        print(f"Could not load inventory: {error}")
        print("Check inventory.json before running again.")
        return

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        try:
            if choice == "1":
                inventory.display_all()

            elif choice == "2":
                add_product_from_input(inventory)

            elif choice == "3":
                product_id = input("Product ID to update: ")
                quantity = int(input("New stock quantity: "))

                if inventory.update_stock(product_id, quantity):
                    print("Stock updated successfully.")
                else:
                    print("Product not found.")

            elif choice == "4":
                product_id = input("Product ID to search: ")
                product = inventory.search_product(product_id)

                if product is None:
                    print("Product not found.")
                else:
                    product.display_information()
                    product.get_supplier().display_information()

            elif choice == "5":
                save_inventory(inventory)

            elif choice == "6":
                save_inventory(inventory)
                print("Goodbye!")
                break

            else:
                print("Invalid choice. Enter 1 to 6.")

        except ValueError as error:
            print(f"Invalid input: {error}")

        except OSError as error:
            print(f"File operation failed: {error}")


if __name__ == "__main__":
    main()