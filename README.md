MiniMart Inventory System

Assignment 1 – Object-Oriented Programming with Python

About the Project

This project is a simple inventory management system for a small store called MiniMart. It uses Object-Oriented Programming (OOP) concepts in Python to manage products, calculate inventory values, and identify products with low stock.

Project Files

* product.py: Contains the Product class, properties, validation, and class methods.
* inventory.py: Contains the Inventory class for adding, removing, finding, and managing products.
* main.py: Contains sample product data and displays the inventory report.

How to Run

1. Install Python 3.10 or newer.
2. Open the project folder in VS Code.
3. Open the Terminal.
4. Run the following command:

py main.py

Design Choices

I used a Product class to represent each product and an Inventory class to manage all products.

A dictionary stores products using their SKU as the key, making it easy to find, add, and remove products.

I used properties and setters to validate price and quantity and prevent invalid values.

The line_value property calculates the total value of each product, while is_low_stock identifies products with a quantity below 5.

Class methods are used to create objects from CSV data and count the number of Product objects created.

A static method is used to validate the SKU format.

Program Output

The program displays an inventory report containing four products: Milk, Bread, Eggs, and Coffee.

* Total inventory value: 104.70
* Low-stock products: Bread (3 left) and Coffee (2 left)
* Product objects created: 4

Requirements

* Python 3.10 or newer
* Python standard library only
* No additional packages required