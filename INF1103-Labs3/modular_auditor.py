def get_valid_input():
    user_input = input("Enter stock quantity (or 'quit' to exit): ").strip()

    if user_input.lower() == "quit":
        return "QUIT"

    if not user_input.isdigit():
        if user_input.startswith("-") and user_input[1:].isdigit():
            print("Error: Negative values are not allowed.")
        else:
            print("Error: Invalid input. Please enter a valid non-negative integer.")
        return "INVALID"

    return int(user_input)


def process_delivery(current_total, new_value):
    return current_total + new_value


def calculate_tax(amount):
    return amount * 0.10


def generate_report(total_units, failed_attempts):
    print("\n=== Audit Summary ===")
    print(f"Total Deliveries Processed (Units): {total_units}")
    print(f"Number of Failed/Rejected Entries: {failed_attempts}")


def main():
    total_inventory = 0
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

        total_inventory = process_delivery(total_inventory, quantity)

        print(f"Added {quantity} units (Tax: {tax:.2f}). Current total: {total_inventory}")

        if total_inventory > 500:
            print("\nALERT: Overstock threshold exceeded (>500 units)! Stopping audit.")
            break

    generate_report(total_inventory, failed_entries)


if __name__ == "__main__":
    main()