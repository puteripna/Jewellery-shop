"""
Program   : ByLuxeItemCatalog.py
Author    : Adam Asyraf bin Roslanzairi (23034493),
            Nur Yasmin Suraya binti Sapar (23038422),
            Puteri Nurin Aisya binti Ainul Hasni (23035742)
Date      : 27 April 2024

Product-specific catalog window which displays description of the product and its stock availability
and allows users to order products.

Features included:
    1. Enter quantity of products to be ordered.
    2. Reduce stock availability and update stock availability data in file.
    2. Saves order data to file.
    3. Return to main catalog page.
"""

from breezypythongui import EasyFrame
from tkinter import PhotoImage
from tkinter import messagebox
from json.decoder import JSONDecodeError
import json


class catalogItem(EasyFrame):
    def __init__(self, USERNAME):
        super().__init__()
        self.USERNAME = USERNAME

    def catalogAnklet(self):
        EasyFrame.__init__(self, title = "Anklet Catalog", width = 525, height = 400)
        self.setBackground("#45523e")
        item = "Anklet"

        # ======== LABELS ========
        nameAnklet = self.addLabel (text = "Anklet ˖✧", row = 0, column = 0, sticky = "NSW", columnspan = 2)
        nameAnklet["font"] = ("TIMES", 22, "bold")
        nameAnklet["foreground"] = "white"
        nameAnklet["background"] = "#45523e"

        descPanel1 = self.addPanel(row = 1, column = 0, columnspan = 2, background = "#f5ece5")

        # Photo
        firstItem = descPanel1.addLabel(text = "", row=0, column=1, rowspan = 3, sticky = "NSEW")
        descPanel1.image1 = PhotoImage(file = "janklet.gif")
        firstItem["image"] = descPanel1.image1
        firstItem["background"] = "#f5ece5"

        # ROW 1
        ankletRow1 = descPanel1.addLabel(text = "RM15.00",row = 0, column = 0, sticky = "W",)
        ankletRow1["font"] = ("TIMES", 17)
        ankletRow1["foreground"] = "black"
        ankletRow1["background"] = "#f5ece5"

        # ROW 2
        ankletRow2 = descPanel1.addLabel(text = "Descriptions: \n- Stainless steel \n- PVD coating     ",
                                         row = 1, column = 0, columnspan = 2)
        ankletRow2["font"] = ("HELVETICA", 12)
        ankletRow2["foreground"] = "black"
        ankletRow2["background"] = "#f5ece5"

        # ROW 3
        ankletRow3 = descPanel1.addLabel(text = "Measurements of Item: \n- Length size: 22 - 26 cm",
                                         row = 2, column = 0, columnspan = 2)
        ankletRow3["font"] = ("HELVETICA", 12)
        ankletRow3["foreground"] = "black"
        ankletRow3["background"] = "#f5ece5"

        # ROW 4
        ankletRow4 = descPanel1.addLabel(text = "Item Availability: ", sticky = "NSEW", row = 3, column = 0)
        descPanel1.addIntegerField(value = itemCheck(item), row = 3, column = 1, sticky = "W", state = "readonly")
        ankletRow4["font"] = ("HELVETICA", 12)
        ankletRow4["foreground"] = "black"
        ankletRow4["background"] = "#f5ece5"

        # ROW 5
        ankletRow5 = descPanel1.addLabel(text = "Place Order: ", sticky = "NSEW", row = 4, column = 0)
        self.valueAnklet = descPanel1.addIntegerField(value = 0, row = 4, column = 1, sticky = "W")
        ankletRow5["font"] = ("HELVETICA", 12)
        ankletRow5["foreground"] = "black"
        ankletRow5["background"] = "#f5ece5"

        # ======== BUTTONS ========
        # ROW 6
        descPanel1.addButton(
                            text="Confirm Order!", row=5, column=0, columnspan=2,
                            command=lambda : self.loopedAnklet(item)  # Use lambda to delay execution
                            )

        descPanel1.addButton(
                            text="Back", row=5, column=1, columnspan=2,
                            command=self.loopedMain
                            )

    def catalogBracelet(self):
        EasyFrame.__init__(self, title = "Bracelet Catalog", width = 525, height = 400)
        self.setBackground("#45523e")
        item = "Bracelet"

        nameBracelet = self.addLabel(text = "Bracelet ˖✧", row = 0, column = 0, sticky = "NSW", columnspan = 2)
        nameBracelet["font"] = ("TIMES", 22,"bold")
        nameBracelet["foreground"] = "white"
        nameBracelet["background"] = "#45523e"

        descPanel1 = self.addPanel(row = 1, column = 0, columnspan = 2, background = "#f5ece5")

        #Photo
        secItem = descPanel1.addLabel(text = "", row=0, column=1, rowspan = 3, sticky = "NSEW")
        descPanel1.image1 = PhotoImage(file = "jbracelet.gif")
        secItem["image"] = descPanel1.image1
        secItem["background"] = "#f5ece5"

        #ROW 1
        BraceletRow1 = descPanel1.addLabel(text = "RM15.00", row = 0, column = 0, sticky = "W")
        BraceletRow1["font"] = ("TIMES", 17)
        BraceletRow1["foreground"] = "black"
        BraceletRow1["background"] = "#f5ece5"

        #ROW 2
        BraceletRow2 = descPanel1.addLabel(text = "Descriptions: \n- Stainless steel  \n- Rhodium plated",
                                           row = 1, column = 0, columnspan = 2)
        BraceletRow2["font"] = ("HELVETICA", 12)
        BraceletRow2["foreground"] = "black"
        BraceletRow2["background"] = "#f5ece5"

        #ROW 3
        BraceletRow3 = descPanel1.addLabel(text = "Measurements of Item: \n- Length size: 17 - 21 cm\n"
                                                  "- Pendant size: 1.2 cm    ",
                                           row = 2, column = 0, columnspan = 2)
        BraceletRow3["font"] = ("HELVETICA", 12)
        BraceletRow3["foreground"] = "black"
        BraceletRow3["background"] = "#f5ece5"

        #ROW 4
        BraceletRow4 = descPanel1.addLabel(text = "Item Availability: ", sticky = "NSEW", row = 3, column = 0)
        descPanel1.addIntegerField(value = itemCheck(item), row = 3, column = 1, sticky = "W", state = "readonly")
        BraceletRow4["font"] = ("HELVETICA", 12)
        BraceletRow4["foreground"] = "black"
        BraceletRow4["background"] = "#f5ece5"

        #ROW 5
        BraceletRow5 = descPanel1.addLabel(text = "Place Order: ", sticky = "NSEW", row = 4, column = 0)
        self.valueBracelet = descPanel1.addIntegerField(value = 0, row = 4, column = 1, sticky = "W")
        BraceletRow5["font"] = ("HELVETICA", 12)
        BraceletRow5["foreground"] = "black"
        BraceletRow5["background"] = "#f5ece5"

        #ROW 6
        descPanel1.addButton(
                            text="Confirm Order!", row=5, column=0, columnspan=2,
                            command=lambda: self.loopedBracelet(item)  # Use lambda to delay execution
                            )

        descPanel1.addButton(
                            text="Back", row=5, column=1, columnspan=2,
                            command=self.loopedMain
                            )

    def catalogEarring(self):
        EasyFrame.__init__(self, title = "Earring Catalog", width = 525, height = 400)
        self.setBackground("#45523e")
        item = "Earrings"

        nameEarring = self.addLabel(text = "Earring ˖✧", row = 0, column = 0,sticky = "NSW", columnspan = 2)
        nameEarring["font"] = ("TIMES", 22,"bold")
        nameEarring["foreground"] = "white"
        nameEarring["background"] = "#45523e"

        descPanel1 = self.addPanel(row = 1, column = 0, columnspan = 2, background = "#f5ece5")

        #Photo
        thirdItem = descPanel1.addLabel(text = "", row=0, column=1, rowspan = 3, sticky = "NSEW")
        descPanel1.image1 = PhotoImage(file = "jearring.gif")
        thirdItem["image"] = descPanel1.image1
        thirdItem["background"] = "#f5ece5"

        #ROW 1
        EarringRow1 = descPanel1.addLabel(text = "RM15.00", row = 0, column = 0, sticky = "W")
        EarringRow1["font"] = ("TIMES", 17)
        EarringRow1["foreground"] = "black"
        EarringRow1["background"] = "#f5ece5"

        #ROW 2
        EarringRow2 = descPanel1.addLabel(text = "Descriptions: \n- Brass  \n- PVD coating",
                                          row = 1, column = 0, columnspan = 2)
        EarringRow2["font"] = ("HELVETICA", 12)
        EarringRow2["foreground"] = "black"
        EarringRow2["background"] = "#f5ece5"

        #ROW 3
        EarringRow3 = descPanel1.addLabel(text = "Measurements of Item: \n- Length: 1.4 cm\t\n- Width: 1.6 cm\t",
                                          row = 2, column = 0, columnspan = 2)
        EarringRow3["font"] = ("HELVETICA", 12)
        EarringRow3["foreground"] = "black"
        EarringRow3["background"] = "#f5ece5"

        #ROW 4
        EarringRow4 = descPanel1.addLabel(text = "Item Availability: ", sticky = "NSEW", row = 3, column = 0)
        descPanel1.addIntegerField(value = itemCheck(item), row = 3, column = 1, sticky = "W", state = "readonly")
        EarringRow4["font"] = ("HELVETICA", 12)
        EarringRow4["foreground"] = "black"
        EarringRow4["background"] = "#f5ece5"

        #ROW 5
        EarringRow5 = descPanel1.addLabel(text = "Place Order: ", sticky = "NSEW", row = 4, column = 0)
        self.valueEarring = descPanel1.addIntegerField(value = 0, row = 4, column = 1, sticky = "W")
        EarringRow5["font"] = ("HELVETICA", 12)
        EarringRow5["foreground"] = "black"
        EarringRow5["background"] = "#f5ece5"

        #ROW 6
        descPanel1.addButton(
                            text="Confirm Order!", row=5, column=0, columnspan=2,
                            command=lambda: self.loopedEarring(item)  # Use lambda to delay execution
                            )

        descPanel1.addButton(
                            text="Back", row=5, column=1, columnspan=2,
                            command=self.loopedMain
                            )

    def catalogNecklace(self):
        EasyFrame.__init__(self, title = "Necklace Catalog", width = 525, height = 400)
        self.setBackground("#45523e")
        item = "Necklace"

        nameNecklace = self.addLabel(text = "Necklace ˖✧", row = 0, column = 0,sticky = "NSW", columnspan = 2)
        nameNecklace["font"] = ("TIMES", 22, "bold")
        nameNecklace["foreground"] = "white"
        nameNecklace["background"] = "#45523e"

        descPanel1 = self.addPanel(row = 1, column = 0, columnspan = 2, background = "#f5ece5")

        #Photo
        fourthItem = descPanel1.addLabel(text = "", row=0, column=1, rowspan = 3, sticky = "NSEW")
        descPanel1.image1 = PhotoImage(file = "jnecklace.gif")
        fourthItem["image"] = descPanel1.image1
        fourthItem["background"] = "#f5ece5"

        #ROW 1
        NecklaceRow1 = descPanel1.addLabel(text = "RM25.00",  row = 0, column = 0, sticky = "W")
        NecklaceRow1["font"] = ("TIMES", 17)
        NecklaceRow1["foreground"] = "black"
        NecklaceRow1["background"] = "#f5ece5"

        #ROW 2
        NecklaceRow2 = descPanel1.addLabel(text = "Descriptions:\n- Brass  \n- Cubic zirconia",
                                           row = 1, column = 0, columnspan = 2)
        NecklaceRow2["font"] = ("HELVETICA", 12)
        NecklaceRow2["foreground"] = "black"
        NecklaceRow2["background"] = "#f5ece5"

        #ROW 3
        NecklaceRow3 = descPanel1.addLabel(text ="Measurements of Item: \n- Length: 41 - 49 cm \n- Pendant size: 1.3 cm",
                                           row = 2, column = 0, columnspan = 2)
        NecklaceRow3["font"] = ("HELVETICA", 12)
        NecklaceRow3["foreground"] = "black"
        NecklaceRow3["background"] = "#f5ece5"

        #ROW 4
        NecklaceRow4 = descPanel1.addLabel(text = "Item Availability: ", sticky = "NSEW",  row = 3, column = 0)
        descPanel1.addIntegerField (value = itemCheck(item), row = 3, column = 1, sticky = "W", state = "readonly")
        NecklaceRow4["font"] = ("HELVETICA", 12)
        NecklaceRow4["foreground"] = "black"
        NecklaceRow4["background"] = "#f5ece5"

        #ROW 5
        NecklaceRow5 = descPanel1.addLabel(text = "Place Order: ", sticky = "NSEW", row = 4, column = 0)
        self.valueNecklace = descPanel1.addIntegerField (value = 0, row = 4, column = 1, sticky = "W")
        NecklaceRow5["font"] = ("HELVETICA", 12)
        NecklaceRow5["foreground"] = "black"
        NecklaceRow5["background"] = "#f5ece5"

        #ROW 6
        descPanel1.addButton(
                            text="Confirm Order!", row=5, column=0, columnspan=2,
                            command=lambda: self.loopedNecklace(item)  # Use lambda to delay execution
                            )

        descPanel1.addButton(
                            text="Back", row=5, column=1, columnspan=2,
                            command=self.loopedMain
                            )

    def catalogRing(self):
        EasyFrame.__init__(self, title = "Ring Catalog", width = 525, height = 400)
        self.setBackground("#45523e")
        item = "Ring"

        nameRing = self.addLabel(text = "Ring ˖✧", row = 0, column = 0, sticky = "NSW", columnspan = 2)
        nameRing["font"] = ("TIMES", 22,"bold")
        nameRing["foreground"] = "white"
        nameRing["background"] = "#45523e"

        descPanel1 = self.addPanel(row = 1, column = 0, columnspan = 2, background = "#f5ece5")

        #Photo
        fifthItem = descPanel1.addLabel(text = "", row=0, column=1, rowspan = 3, sticky = "NSEW")
        descPanel1.image1 = PhotoImage(file = "jring.gif")
        fifthItem["image"] = descPanel1.image1
        fifthItem["background"] = "#f5ece5"

        #ROW 1
        RingRow1 = descPanel1.addLabel(text = "RM8.00", row = 0, column = 0, sticky = "W")
        RingRow1["font"] = ("TIMES", 17)
        RingRow1["foreground"] = "black"
        RingRow1["background"] = "#f5ece5"

        #ROW 2
        RingRow2 = descPanel1.addLabel(text = "Descriptions: \n- Brass  \n- Cubic zirconia",
                                       row = 1, column = 0, columnspan = 2)
        RingRow2["font"] = ("HELVETICA", 12)
        RingRow2["foreground"] = "black"
        RingRow2["background"] = "#f5ece5"

        #ROW 3
        RingRow3 = descPanel1.addLabel(text = "Measurements of Item: \n- Adjustable size: US 6.5-7\n- Width: 0.6 cm",
                                      row = 2, column = 0, columnspan = 2)
        RingRow3["font"] = ("HELVETICA", 12)
        RingRow3["foreground"] = "black"
        RingRow3["background"] = "#f5ece5"

        #ROW 4
        RingRow4 = descPanel1.addLabel(text = "Item Availability: ", sticky = "NSEW",  row = 3, column = 0)
        descPanel1.addIntegerField(value = itemCheck(item), row = 3, column = 1, sticky = "W", state = "readonly")
        RingRow4["font"] = ("HELVETICA", 12)
        RingRow4["foreground"] = "black"
        RingRow4["background"] = "#f5ece5"

        #ROW 5
        RingRow5 = descPanel1.addLabel(text = "Place Order: ", sticky = "NSEW",  row = 4, column = 0)
        self.valueRing = descPanel1.addIntegerField (value = 0, row = 4, column = 1, sticky = "W")
        RingRow5["font"] = ("HELVETICA", 12)
        RingRow5["foreground"] = "black"
        RingRow5["background"] = "#f5ece5"

        #ROW 6
        descPanel1.addButton(
                            text="Confirm Order!", row=5, column=0, columnspan=2,
                            command=lambda: self.loopedRing(item)  # Use lambda to delay execution
                            )

        descPanel1.addButton(
                            text="Back", row=5, column=1, columnspan=2,
                            command=self.loopedMain
                            )

    def catalogWatch(self):
        EasyFrame.__init__(self, title = "Watch Catalog",
                           width = 525, height = 400)
        self.setBackground("#45523e")
        item = "Watch"

        nameWatch = self.addLabel(text = "Watch ˖✧", row = 0, column = 0,sticky = "NSW", columnspan = 2)
        nameWatch["font"] = ("TIMES", 22,"bold")
        nameWatch["foreground"] = "white"
        nameWatch["background"] = "#45523e"

        descPanel1 = self.addPanel(row = 1, column = 0, columnspan = 2, background = "#f5ece5")

        #Photo
        sixthItem = descPanel1.addLabel(text = "", row=0, column=1, rowspan = 3, sticky = "NSEW")
        descPanel1.image1 = PhotoImage(file = "jwatch.gif")
        sixthItem["image"] = descPanel1.image1
        sixthItem["background"] = "#f5ece5"

        #ROW 1
        WatchRow1 = descPanel1.addLabel(text = "RM35.00", row = 0, column = 0, sticky = "W")
        WatchRow1["font"] = ("TIMES", 17)
        WatchRow1["foreground"] = "black"
        WatchRow1["background"] = "#f5ece5"

        #ROW 2
        WatchRow2 = descPanel1.addLabel(text = "Descriptions: \n- Stainless steel  \n- Quartz",
                                        row = 1, column = 0, columnspan = 2)
        WatchRow2["font"] = ("HELVETICA", 12)
        WatchRow2["foreground"] = "black"
        WatchRow2["background"] = "#f5ece5"

        #ROW 3
        WatchRow3 = descPanel1.addLabel(text = "Measurements of Item: \n- Strap width: 12 mm\t",
                                        row = 2, column = 0, columnspan = 2)
        WatchRow3["font"] = ("HELVETICA", 12)
        WatchRow3["foreground"] = "black"
        WatchRow3["background"] = "#f5ece5"

        #ROW 4
        WatchRow4 = descPanel1.addLabel(text = "Item Availability: ", sticky = "NSEW", row = 3, column = 0)
        descPanel1.addIntegerField(value = itemCheck(item), row = 3, column = 1, sticky = "W", state = "readonly")
        WatchRow4["font"] = ("HELVETICA", 12)
        WatchRow4["foreground"] = "black"
        WatchRow4["background"] = "#f5ece5"

        #ROW 5
        WatchRow5 = descPanel1.addLabel(text = "Place Order: ", sticky = "NSEW",  row = 4, column = 0)
        self.valueWatch = descPanel1.addIntegerField(value = 0, row = 4, column = 1, sticky = "W")
        WatchRow5["font"] = ("HELVETICA", 12)
        WatchRow5["foreground"] = "black"
        WatchRow5["background"] = "#f5ece5"

        #ROW 6
        descPanel1.addButton(
                            text="Confirm Order!", row=5, column=0, columnspan=2,
                            command=lambda: self.loopedWatch(item)  # Use lambda to delay execution
                            )

        descPanel1.addButton(
                            text="Back", row=5, column=1, columnspan=2,
                            command=self.loopedMain
                            )

    def loopedAnklet(self, item):
        # Get quantity from user
        quantity = self.valueAnklet.getNumber()
        # Check if quantity is valid
        self.checkQty(quantity, item)

    def loopedBracelet(self, item):
        quantity = self.valueBracelet.getNumber()
        self.checkQty(quantity, item)

    def loopedEarring(self, item):
        quantity = self.valueEarring.getNumber()
        self.checkQty(quantity, item)

    def loopedNecklace(self, item):
        quantity = self.valueNecklace.getNumber()
        self.checkQty(quantity, item)

    def loopedRing(self, item):
        quantity = self.valueRing.getNumber()
        self.checkQty(quantity, item)

    def loopedWatch(self, item):
        quantity = self.valueWatch.getNumber()
        self.checkQty(quantity, item)

    def checkQty(self, quantity, item):
        """ Check if input of quantity is valid and if invalid, let user re-input quantity. """

        # Read current stock availability from file
        with open("stock.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                storedItem, stock = line.strip().split(',')
                if storedItem == item:
                    STOCK = int(stock)

        # Check if quantity is in valid range
        if 0 < quantity <= STOCK:
            # Add item to cart and reduce stock
            self.addToCart(item, quantity)
            self.reduceStock(item, quantity)

        elif quantity < 0:
            # Show error message for negative quantity
            messagebox.showerror(
                                title="Error",
                                message="Quantity of order placed must be more than 0.\nPlease re-enter your choice."
                                )
            # Destroy current window and return to catalog for the specified item
            self.destroy()
            catalog_method_name = f"catalog{item.capitalize()}"
            getattr(self, catalog_method_name)()
            self.update_idletasks()  # Make widgets reappear

        elif quantity > STOCK:
            # Show error message for quantity exceeding stock limit
            messagebox.showerror(
                                title="Error",
                                message="Sorry, your order currently exceeds stock limit.\nPlease re-enter your choice."
                                )
            # Destroy current window and return to catalog for the specified item
            self.destroy()
            catalog_method_name = f"catalog{item.capitalize()}"
            getattr(self, catalog_method_name)()
            self.update_idletasks()  # Make widgets reappear


    def addToCart(self, item, quantity):
        """ Write products added to cart in a file """

        if quantity <= 0:
            return
        try:
            # Read existing cart order file
            with open("cart.txt", "r") as file:
                try:
                    user_cart = json.load(file)
                except JSONDecodeError:
                    user_cart = {}
        except FileNotFoundError:
            # If file doesn't exist, initialize cart order data
            user_cart = {}

        if self.USERNAME not in user_cart:
            # If user has no existing cart order, create new entry
            user_cart[self.USERNAME] = {"item": [item], "quantity": [quantity]}
        else:
            # If user already has existing cart order, append new order
            user_cart[self.USERNAME]["item"].append(item)
            user_cart[self.USERNAME]["quantity"].append(quantity)

        # Write updated cart order data to file
        with open("cart.txt", "w") as file:
            json.dump(user_cart, file, indent=4)  # Indent for pretty formatting


    def reduceStock(self, item, quantity):
        """ Reduce stock availability """

        try:
            # Read current stock availability from file
            with open("stock.txt", "r") as file:
                lines = file.readlines()

            updated_lines = []
            found = False

            for line in lines:
                storedItem, storedQty = line.strip().split(',')
                if storedItem == item:
                    # Reduce current stock with number of products user placed order for
                    storedQty = int(storedQty) - quantity
                    updated_lines.append(f"{storedItem},{storedQty}\n")
                    found = True
                else:
                    updated_lines.append(line)

            if not found:
                print(item, "not found in stock file.")
                return

            # Write updated stock availability data to file
            with open("stock.txt", "w") as file:
                file.writelines(updated_lines)
                self.master.destroy()
                from ByLuxeCatalog import catalogMain
                catalogMain(self.USERNAME)

        except FileNotFoundError:
            print("Stock file not found.")
            from ByLuxeCatalog import catalogMain
            catalogMain(self.USERNAME)


    def loopedMain(self):
        self.master.destroy()
        from ByLuxeCatalog import catalogMain
        catalogMain(self.USERNAME)


def itemCheck(item):
    """ Check number of item stock availability to be displayed"""

    with open("stock.txt", "r") as file:
        for line in file:
            storedItem, storedQty = line.strip().split(',')
            if item == storedItem:
                return int(storedQty)
    return False
