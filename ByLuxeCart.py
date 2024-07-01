"""
Program   : ByLuxeCart_old.py
Author    : Nur Yasmin Suraya binti Sapar (23038422),
            Nur Izzaty binti Yaacob (23039735)
Date      : 27 April 2024

Checkout point for users to place order or remove orders.

Files used:
    1. "PriceList.txt":
    2. "User_account.txt":
    3. "cart.txt":
Features included:
    1. Reads user data from file to display user details
    2. Reads order data from file to display product, item and quantity.
    3. Computes subtotal and total payment.
    4. Deletes order data from file and updates stock in file if user removes order.
    5. Saves order data to order history file if user places orders.
    6. Return to main catalog page.
"""

import tkinter as tk
from tkinter import messagebox
import json
from breezypythongui import EasyFrame


class Cart(EasyFrame):
    def __init__(self, USERNAME):
        self.USERNAME = USERNAME

        EasyFrame.__init__(self, title="ByLuxe Cart",
                           width=400, height=500)
        self.setBackground("#f5ece5")

        cartLabel = self.addLabel(text="Shopping Cart", row=0, column=0,
                                  sticky="NSEW", columnspan=3)
        cartLabel["font"] = ("TIMES", 20)
        cartLabel["foreground"] = "white"
        cartLabel["background"] = "#45523e"

        # Labels for displaying user information
        self.nameLabel = self.addLabel("", row=1, column=0,
                                       sticky="NSEW", columnspan=3)
        self.nameLabel["font"] = ("TIMES", 10)
        self.nameLabel["foreground"] = "white"
        self.nameLabel["background"] = "#ad7d50"

        self.telLabel = self.addLabel("", row=2, column=0,
                                      sticky="NSEW", columnspan=3)
        self.telLabel["font"] = ("TIMES", 10)
        self.telLabel["foreground"] = "white"
        self.telLabel["background"] = "#ad7d50"

        self.addressLabel = self.addLabel("", row=3, column=0,
                                          sticky="NSEW", columnspan=3)
        self.addressLabel["font"] = ("TIMES", 10)
        self.addressLabel["foreground"] = "white"
        self.addressLabel["background"] = "#ad7d50"

        # Load user information from file
        self.loadUserInfo("user_account.txt")

        self.products = []

        self.outputArea = self.addTextArea("", row=4, column=0,
                                           columnspan=5,
                                           width=50, height=15)
        self.loadProductInfo("cart.txt")

        # Buttons to place order or back to catalog
        self.placeOrder = self.addButton(text="Place Order", row=5, column=0, command=self.placeOrder)
        self.removeAll = self.addButton(text="Remove all", row=5, column=1, command=self.addStock)
        self.back = self.addButton(text="Back", row=5, column=2, command=self.back)

    def loadUserInfo(self, userfile):
        """  Load user info from file to display user information for checkout """
        try:
            # Read user accounts from file
            with open(userfile, "r") as file:
                users = json.load(file)
                # Get user information associated with username
                user = users.get(self.USERNAME, {})
                # Display user informations
                self.nameLabel["text"] = "Name : " + user.get("name", "")
                self.telLabel["text"] = "Contact No : " + user.get("numfon", "")
                self.addressLabel["text"] = "Address : " + user.get("address", "")

        except FileNotFoundError:
            messagebox.showerror("Error", "User information file not found.")

    def loadProductInfo(self, cartfile):
        """ Load product info to text area from file """

        # Obtain and validate the inputs
        shippingFee = 4.9
        subtotal = 0.0
        totalPayment = 0.0

        try:
            # Read user's cart order
            with open(cartfile, "r") as file:
                users = json.load(file)
                # Get user's product and quantity added in cart
                product_info = users.get(self.USERNAME, {})
                product_list = product_info.get("item", [])
                quantity_list = product_info.get("quantity", [])
        except FileNotFoundError:
            messagebox.showerror("Error", "Product information file not found.")

        try:
            with open("PriceList.txt", "r") as price_file:
                prices = json.load(price_file)
        except FileNotFoundError:
            messagebox.showerror("Error", "Product price information file not found.")

        # Set header
        result = "%-10s%-10s%-10s\n" % ("Product", "Price", "Quantity")

        # Output result
        for product, quantity in zip(product_list, quantity_list):
            price_info = prices.get(product, {})  # Get price list for all products available in catalog
            price = float(price_info.get("price", 0))  # Get price for specific product in user's cart
            subtotal += price * int(quantity)
            result += "%-10s%-10.2f%-10d\n" % (product, price, int(quantity))

        totalPayment = subtotal + shippingFee
        result += "\nSubtotal     : RM%0.2f\n" % subtotal
        result += "Shipping Fee : RM 4.90\n"
        result += "Total Payment: RM%0.2f\n" % totalPayment

        self.outputArea.setText(result)

    def back(self):
        # Back to main catalog
        from ByLuxeCatalog import catalogMain
        self.master.destroy()
        catalogMain(self.USERNAME)

    def removeOrder(self):
        """ Delete current order in cart """
        cartfile = "cart.txt"

        # Clear out the whole text box
        self.outputArea.delete('1.0', tk.END)

        # Delete user's cart data from file
        try:
            with open(cartfile, "r") as file:
                cart_data = json.load(file)
        except FileNotFoundError:
            messagebox.showerror("Error", "Cart information file not found.")

        if self.USERNAME in cart_data:
            del cart_data[self.USERNAME]

        with open(cartfile, "w") as file:
            json.dump(cart_data, file, indent=4)
        # Refresh the text box to reappear header and footer
        self.loadProductInfo(cartfile)

    def addStock(self):
        cartfile = "cart.txt"
        try:
            with open(cartfile, "r") as file:
                cart_data = json.load(file)
        except FileNotFoundError:
            messagebox.showerror("Error", "Cart information file not found.")

        if self.USERNAME in cart_data:
            removed_items = cart_data[self.USERNAME].get("item", [])
            removed_quantities = cart_data[self.USERNAME].get("quantity", [])

            try:
                # Read current stock availability from file
                with open("stock.txt", "r") as file:
                    lines = file.readlines()

                updated_lines = []
                found = False

                for line in lines:
                    storedItem, storedQty = line.strip().split(',')
                    for item, quantity in zip(removed_items, removed_quantities):
                        if storedItem == item:
                            # Add back the removed quantity to the stock
                            storedQty = int(storedQty) + int(quantity)
                            updated_lines.append(f"{storedItem},{storedQty}\n")
                            found = True
                        else:
                            updated_lines.append(line)
                if not found:
                    print("Item not found in stock file.")
                    return

                # Write updated stock availability data to file
                with open("stock.txt", "w") as file:
                    file.writelines(updated_lines)

            except FileNotFoundError:
                messagebox.showerror("Error", "Stock information file not found.")

        self.removeOrder()

    def saveOrderHistory(self):
        """ Save orders placed in order history """

        order_history_file = "orderhistory.txt"

        try:
            # Read existing order history file
            with open(order_history_file, "r") as history_file:
                order_history_data = json.load(history_file)
        except FileNotFoundError:
            # If file doesn't exist, initialize order history data
            order_history_data = {}

        try:
            # Read cart file to get the current order
            with open("cart.txt", "r") as cart_file:
                cart_data = json.load(cart_file)
                order_data = cart_data.get(self.USERNAME, {})

                if self.USERNAME not in order_history_data:
                    # If user has no existing order history, create new entry
                    order_history_data[self.USERNAME] = {"item": order_data["item"], "quantity": order_data["quantity"]}
                else:
                    # If user already has existing order history, append new order
                    order_history_data[self.USERNAME]["item"].extend(order_data["item"])
                    order_history_data[self.USERNAME]["quantity"].extend(order_data["quantity"])

            # Write updated order history data to file
            with open(order_history_file, "w") as history_file:
                json.dump(order_history_data, history_file, indent=4)

        except FileNotFoundError:
            messagebox.showerror("Error", "Cart information file not found.")

    def placeOrder(self):
        from ByLuxeCatalog import catalogMain
        cartfile = "cart.txt"

        try:
            with open(cartfile, "r") as file:
                cart_data = json.load(file)
        except FileNotFoundError:
            messagebox.showerror("Error", "Cart information file not found.")

        if self.USERNAME not in cart_data:
            # Output error message if no products have been added in the cart
            messagebox.showerror(title="Cart error", message="No products found in cart. \n"
                                                             "Please add product to cart to proceed.")
        else:
            messagebox.showinfo("Place Order", "Your order has been placed!")
            self.saveOrderHistory()
            self.removeOrder()
            self.master.destroy()
            catalogMain(self.USERNAME)
