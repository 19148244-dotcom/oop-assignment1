from inventory import Inventory

from product import Product

SAMPLE = [

    "Milk,MLK001,1.25,12",

    "Bread,BRD002,0.90,3",

    "Eggs,EGG003,2.40,30",

    "Coffee,COF004,7.50,2",

]

def main():

    inventory = Inventory.from_lines(SAMPLE)

    print("MiniMart Inventory Report")

    print("-" * 45)

    print(f"{'Product':<12}{'SKU':<10}{'Price':>8}{'Qty':>6}{'Value':>9}")

    print("-" * 45)

    for product in inventory.products.values():

        print(

            f"{product.name:<12}{product.sku:<10}"

            f"{product.price:>8.2f}"

            f"{product.quantity:>6}"

            f"{product.line_value:>9.2f}"

        )

    print("-" * 45)

    print(f"Total inventory value: {inventory.total_value():.2f}")

    print("\nLow stock products (quantity below 5):")

    for product in inventory.products.values():

        if product.is_low_stock:

            print(f"- {product.name}: {product.quantity} left")

    print(f"\nProduct objects created: {Product.count()}")

if __name__ == "__main__":

    main()
