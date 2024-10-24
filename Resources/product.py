


class Product():
    def __init__(self, product_id, product_name, product_description, quantity, ppu) -> None:
        self.product_id = product_id
        self.product_name = product_name
        self.product_description = product_description
        self.quantity = quantity
        self.ppu = ppu

    def ReturnAttr(self):
        all_attr = []
        all_attr.append(self.product_name)
        all_attr.append(self.product_description)
        all_attr.append(self.quantity)
        all_attr.append(self.ppu)

        return all_attr