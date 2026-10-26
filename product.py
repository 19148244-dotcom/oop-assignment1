import math

import re

class Product:

    product_count = 0

    def __init__(self, name, sku, price, quantity):

        if not isinstance(name, str) or not name.strip():

            raise ValueError("Product name must not be empty")

        if not self.is_valid_sku(sku):

            raise ValueError("Invalid SKU")

        self.name = name

        self.sku = sku

        self.price = price

        self.quantity = quantity

        Product.product_count += 1

    def __repr__(self):

        return (

            f"Product({self.name!r}, {self.sku!r}, "

            f"{self.price!r}, {self.quantity!r})"

        )

    @property

    def price(self):

        return self._price

    @price.setter

    def price(self, value):

        if isinstance(value, bool) or not isinstance(value, (int, float)):

            raise TypeError("Price must be a number")

        if not math.isfinite(value):

            raise ValueError("Price must be finite")

        if value < 0:

            raise ValueError("Price cannot be negative")

        self._price = value

    @property

    def quantity(self):

        return self._quantity

    @quantity.setter

    def quantity(self, value):

        if type(value) is not int:

            raise TypeError("Quantity must be an integer")

        if value < 0:

            raise ValueError("Quantity cannot be negative")

        self._quantity = value

    @property

    def line_value(self):

        return self.price * self.quantity

    @property

    def is_low_stock(self):

        return self.quantity < 5

    @classmethod

    def from_csv_line(cls, line):

        parts = line.strip().split(",")

        if len(parts) != 4:

            raise ValueError("A CSV line must have four values")

        name, sku, price, quantity = [

            part.strip() for part in parts

        ]

        return cls(name, sku, float(price), int(quantity))

    @staticmethod

    def is_valid_sku(sku):

        return (

            isinstance(sku, str)

            and re.fullmatch(r"[A-Za-z]{3}[0-9]{3}", sku) is not None

        )

    @classmethod

    def count(cls):

        return cls.product_count