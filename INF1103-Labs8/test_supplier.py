from digital_product import DigitalProduct
from physical_product import PhysicalProduct
from supplier import Supplier

supplier = Supplier("S001", "Test Supplier", "test@example.com")

mouse = PhysicalProduct("P800", "Test Mouse", 15.50, 10, 0.2, supplier)
ebook = DigitalProduct("D800", "Test E-book", 9.90, 20, 25.0, supplier)

del supplier

mouse.get_supplier().display_information()
ebook.get_supplier().display_information()

print("Same supplier object?", mouse.get_supplier() is ebook.get_supplier())