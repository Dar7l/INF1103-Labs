import os

FILENAME = "inventory.txt"


def get_valid_input():
    user_input = input("Enter stock quantity (or 'quit' to exit): ").strip()

    if user_input.lower() == "quit":
        return "QUIT"

    if not user_input.isdigit():
        if user_input.startswith("-") and user_input[1:].isdigit():
            print("Error: Negative values are not allowed.")
        else:
            print(
                "Error: Invalid input. Please enter a valid non-negative integer."
            )
        return "INVALID"

    return int(user_input)


def process_delivery(current_total, new_value):
    return current_total + new_value


def calculate_tax(amount):
    return amount * 0.10


def load_inventory():
    """Reads previously saved transactions from inventory.txt on startup."""
    history = []
    if not os.path.exists(FILENAME):
        print(f"No existing {FILENAME} found. Starting with clean inventory.")
        return history, 0

    try:
        with open(FILENAME, "r") as file:
            for line in file:
                cleaned = line.strip()
                if cleaned.isdigit():
                    history.append(int(cleaned))

        total = sum(history)
        print(
            f"Loaded existing inventory from {FILENAME}. Current total: {total} units."
        )
        return history, total
    except Exception as e:
        print(f"Error reading {FILENAME}: {e}. Starting fresh.")
        return [], 0


def save_inventory(history):
    """Saves the transaction history list to inventory.txt on program exit."""
    try:
        with open(FILENAME, "w") as file:
            for item in history:
                file.write(f"{item}\n")
        print(f"\nInventory successfully saved to {FILENAME}")
    except Exception as e:
        print(f"Error saving inventory: {e}")


def generate_report(total_units, failed_attempts):
    print("\n=== Audit Summary ===")
    print(f"Total Deliveries Processed (Units): {total_units}")
    print(f"Number of Failed/Rejected Entries: {failed_attempts}")


def main():
    history_list, total_inventory = load_inventory()
    failed_entries = 0

    print("=== Smart Inventory Auditor ===")

    while True:
        result = get_valid_input()

        if result == "QUIT":
            break

        if result == "INVALID":
            failed_entries += 1
            continue

        quantity = result
        tax = calculate_tax(quantity)

        history_list.append(quantity)
        total_inventory = process_delivery(total_inventory, quantity)

        print(
            f"Added {quantity} units (Tax: {tax:.2f}). Current total: {total_inventory}"
        )
        print(f"Transaction History: {history_list}\n")

        if total_inventory > 500:
            print(
                "\nALERT: Overstock threshold exceeded (>500 units)! Stopping audit."
            )
            break

    # Save transaction history and print final summary
    save_inventory(history_list)
    generate_report(total_inventory, failed_entries)


if __name__ == "__main__":
    main()