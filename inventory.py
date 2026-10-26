from product import Product

class Inventory:

     def __init__(self):

        self.products = {}

     def add(self, product):

         if not isinstance(product, Product):

            raise TypeError("Expected a Product")

         self.products[product.sku] = product

     def remove(self, sku):

         return self.products.pop(sku, None)

     def find(self, sku):

         return self.products.get(sku)

     def total_value(self):

         total = 0

         for product in self.products.values():

             total += product.line_value

         return total

     @classmethod

     def from_lines(cls, lines):

         inventory = cls()

         for line in lines:

            product = Product.from_csv_line(line)

            inventory.add(product)

         return inventory