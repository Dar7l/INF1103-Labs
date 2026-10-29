import json

from product import Product
from inventory import Inventory


FILENAME = "inventory.json"


def load_inventory():
    inventory = Inventory()

    try:
        with open(FILENAME, "r", encoding="utf-8") as file:
            records = json.load(file)

    except FileNotFoundError:
        print("inventory.json not found. Starting with empty inventory.")
        return inventory

    if not isinstance(records, list):
        raise ValueError("inventory.json must contain a list of products.")

    for record in records:
        # Accept both ID/Name/Price/Stock and id/name/price/stock.
        record = {
            key.lower(): value
            for key, value in record.items()
        }

        product = Product(
            record["id"],
            record["name"],
            float(record["price"]),
            int(record["stock"])
        )

        if not inventory.add_product(product):
            raise ValueError("Duplicate product ID in inventory.json.")

    print("Inventory loaded successfully.")
    return inventory


def save_inventory(inventory):
    records = []

    for product in inventory.get_products():
        records.append(product.to_dict())

    with open(FILENAME, "w", encoding="utf-8") as file:
        json.dump(records, file, indent=4)

    print("Inventory saved successfully.")


def display_menu():
    print("\n=== Inventory Management System ===")
    print("1. Display all products")
    print("2. Add a product")
    print("3. Update stock")
    print("4. Search for a product")
    print("5. Save inventory")
    print("6. Exit")


def main():
    try:
        inventory = load_inventory()

    except (
        OSError,
        ValueError,
        KeyError,
        TypeError,
        AttributeError
    ) as error:
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
                product_id = input("Product ID: ")
                name = input("Product name: ")
                price = float(input("Price: "))
                stock = int(input("Stock quantity: "))

                product = Product(
                    product_id,
                    name,
                    price,
                    stock
                )

                if inventory.add_product(product):
                    print("Product added successfully.")
                else:
                    print("A product with that ID already exists.")

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

            elif choice == "5":
                save_inventory(inventory)

            elif choice == "6":
                save_inventory(inventory)
                print("Goodbye!")
                break

            else:
                print("Invalid choice. Enter a number from 1 to 6.")

        except ValueError as error:
            print(f"Invalid input: {error}")

        except OSError as error:
            print(f"File operation failed: {error}")


if __name__ == "__main__":
    main()