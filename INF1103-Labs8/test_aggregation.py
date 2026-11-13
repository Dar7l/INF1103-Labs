from inventory import Inventory
from physical_product import PhysicalProduct
from supplier import Supplier


supplier = Supplier("S001", "Test Supplier", "test@example.com")
laptop = PhysicalProduct("P100", "Test Laptop", 1200.0, 15, 2.0, supplier)

inventory_a = Inventory()
inventory_b = Inventory()

print("Added to Inventory A?", inventory_a.add_product(laptop))
print("Removed from Inventory A?", inventory_a.remove_product("P100"))
print("Search in Inventory A after removal:", inventory_a.find_product("P100"))

print("\nLaptop details after removal")
laptop.display_information()

print("\nAdded to Inventory B?", inventory_b.add_product(laptop))
print("Same laptop object in Inventory B?", inventory_b.find_product("P100") is laptop)