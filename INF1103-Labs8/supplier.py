class Supplier:
    def __init__(
        self, supplier_id: str, name: str, contact_email: str
    ) -> None:
        self.supplier_id: str = supplier_id
        self.name: str = name
        self.contact_email: str = contact_email

    def display_information(self) -> None:
        print(f"Supplier {self.supplier_id}: {self.name}")
        print(f"Contact: {self.contact_email}")

    def to_dict(self) -> dict[str, str]:
        return {
            "supplier_id": self.supplier_id,
            "name": self.name,
            "contact_email": self.contact_email,
        }