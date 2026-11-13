from digital_product import DigitalProduct
from order import Order
from physical_product import PhysicalProduct
from supplier import Supplier


supplier = Supplier("S001", "Test Supplier", "test@example.com")
laptop = PhysicalProduct("P100", "Test Laptop", 1200.0, 15, 2.0, supplier)
ebook = DigitalProduct("D100", "Test E-book", 9.90, 20, 25.0, supplier)

order_a = Order("O001")
order_b = Order("O002")

order_a.add_order_line(laptop, 2)
order_b.add_order_line(laptop, 1)

line_a = order_a.get_order_lines()[0]
line_b = order_b.get_order_lines()[0]

print("Same order line object?", line_a is line_b)
print("Same laptop object?", line_a.product is line_b.product)

order_a.add_order_line(ebook, 1)

print("\nOrder A")
for line in order_a.get_order_lines():
    print(
        f"{line.product.get_product_id()} x{line.quantity}"
        f" = ${line.calculate_subtotal():.2f}"
    )
print(f"Order A total: ${order_a.calculate_total():.2f}")

order_a.remove_order_line(0)

print("\nAfter removing the laptop line from Order A")
print(f"Order A total: ${order_a.calculate_total():.2f}")
print(f"Order B total: ${order_b.calculate_total():.2f}")
print("Order B still refers to the laptop?",
      order_b.get_order_lines()[0].product is laptop)