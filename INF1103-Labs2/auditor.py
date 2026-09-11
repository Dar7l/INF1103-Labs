total_inventory = 0
failed_entries = 0

print("=== Smart Inventory Auditor ===")

while True: 
    user_input = input("Enter stock quantity (or 'quit' to exit):  ").strip()

    if user_input.lower() == "quit":
        break

    if not user_input.isdigit():

        if user_input.startswith("-") and user_input[1:].isdigit():
            print("Error: Negative values are not allowed.")
        else: 
            print("Error: Invalid input. Please enter a valid non-negative integer.")
        failed_entries += 1
        continue

    quantity = int(user_input)

    total_inventory += quantity
    print(f"Added {quantity} units. Current total: {total_inventory}")

    if total_inventory > 500:
        print("\nALERT: Overstock threshold exceeded (>500 units)! Stopping audit.")
        break

print("\n=== Audit Summary ===")
print(f"Total Units Processed: {total_inventory}")
print(f"Number of Failed/Rejected Entries: {failed_entries}")