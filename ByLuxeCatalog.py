"""
Program   : ByLuxeCatalog.py
Author    : Adam Asyraf bin Roslanzairi (23034493),
            Puteri Nurin Aisya binti Ainul Hasni (23035742)
Date      : 27 April 2024

Main catalog page which displays products that users can buy and their prices.
Features included:
    1. Add product to cart which moves application to product-specific catalog window.
    2. Make payment which moves application to cart order window.
    3. Exit program.
"""


from breezypythongui import EasyFrame
from tkinter import PhotoImage
from ByLuxeItemCatalog import catalogItem


class catalogMain(EasyFrame):

    def __init__(self, USERNAME):
        self.USERNAME = USERNAME

        EasyFrame.__init__(self, title="ByLuxe Catalog",
                           width=900, height=700)

        self.master.attributes('-fullscreen', True)

        self.setBackground("#f5ece5")

        companyName = self.addLabel(text="ByLuxe", row=0, column=0, sticky="S", columnspan=3)
        companyName["font"] = ("TIMES", 30, "bold")
        companyName["foreground"] = "black"
        companyName["background"] = "#f5ece5"

        discountLabel = self.addLabel(text="Shop Luxury With Us.", row=1, column=0,
                                      sticky="NSEW", columnspan=3)
        discountLabel["font"] = ("COURIER", 20, "italic")
        discountLabel["foreground"] = "#f5ece5"
        discountLabel["background"] = "#45523e"

        #  ====================================== FIRST LAYER ======================================
        # First Layer Images
        firstItem = self.addLabel(text="", row=2, column=0, sticky="NSEW")
        self.image1 = PhotoImage(file="janklet.gif")
        firstItem["image"] = self.image1
        firstItem["background"] = "#f5ece5"

        secItem = self.addLabel(text="", row=2, column=1, sticky="NSEW")
        self.image2 = PhotoImage(file="jbracelet.gif")
        secItem["image"] = self.image2
        secItem["background"] = "#f5ece5"

        thirdItem = self.addLabel(text="", row=2, column=2, sticky="NSEW")
        self.image3 = PhotoImage(file="jearring.gif")
        thirdItem["image"] = self.image3
        thirdItem["background"] = "#f5ece5"

        # First Layer Naming
        firstItemName = self.addLabel(text="Anklet", row=3, column=0, sticky="NSEW")
        firstItemName["font"] = ("TIMES", 25)
        firstItemName["foreground"] = "black"
        firstItemName["background"] = "#f5ece5"

        secItemName = self.addLabel(text="Bracelet", row=3, column=1, sticky="NSEW")
        secItemName["font"] = ("TIMES", 25)
        secItemName["foreground"] = "black"
        secItemName["background"] = "#f5ece5"

        thirdItemName = self.addLabel(text="Earring", row=3, column=2, sticky="NSEW")
        thirdItemName["font"] = ("TIMES", 25)
        thirdItemName["foreground"] = "black"
        thirdItemName["background"] = "#f5ece5"

        # First Layer Price
        firstItemPrice = self.addLabel(text="RM15.00", row=4, column=0, sticky="N")
        firstItemPrice["font"] = ("Helvetica", 15)
        firstItemPrice["foreground"] = "black"
        firstItemPrice["background"] = "#f5ece5"

        secItemPrice = self.addLabel(text="RM15.00", row=4, column=1, sticky="N")
        secItemPrice["font"] = ("Helvetica", 15)
        secItemPrice["foreground"] = "black"
        secItemPrice["background"] = "#f5ece5"

        thirdItemPrice = self.addLabel \
            (text="RM10.00", row=4, column=2, sticky="N")
        thirdItemPrice["font"] = ("Helvetica", 15)
        thirdItemPrice["foreground"] = "black"
        thirdItemPrice["background"] = "#f5ece5"

        # First Layer Buttons
        self.firstCartItem = self.addButton(text="Add to cart", row=5, column=0,
                                            command=self.openCatalogAnklet)

        self.secCartItem = self.addButton(text="Add to cart", row=5, column=1,
                                          command=self.openCatalogBracelet)

        self.thirdCartItem = self.addButton(text="Add to cart", row=5, column=2,
                                            command=self.openCatalogEarring)

        #  ====================================== SECOND LAYER ======================================
        # Sec Layer Images
        fourthItem = self.addLabel(text="", row=6, column=0, sticky="NSEW")
        self.image4 = PhotoImage(file="jnecklace.gif")
        fourthItem["image"] = self.image4
        fourthItem["background"] = "#f5ece5"

        fifthItem = self.addLabel(text="", row=6, column=1, sticky="NSEW")
        self.image5 = PhotoImage(file="jring.gif")
        fifthItem["image"] = self.image5
        fifthItem["background"] = "#f5ece5"

        sixthItem = self.addLabel(text="", row=6, column=2, sticky="NSEW")
        self.image6 = PhotoImage(file="jwatch.gif")
        sixthItem["image"] = self.image6
        sixthItem["background"] = "#f5ece5"

        # Sec Layer Naming
        fourthItemName = self.addLabel(text="Necklace", row=7, column=0, sticky="NSEW")
        fourthItemName["font"] = ("TIMES", 25)
        fourthItemName["foreground"] = "black"
        fourthItemName["background"] = "#f5ece5"

        fifthItemName = self.addLabel(text="Ring", row=7, column=1, sticky="NSEW")
        fifthItemName["font"] = ("TIMES", 25)
        fifthItemName["foreground"] = "black"
        fifthItemName["background"] = "#f5ece5"

        sixthItemName = self.addLabel(text="Watch", row=7, column=2, sticky="NSEW")
        sixthItemName["font"] = ("TIMES", 25)
        sixthItemName["foreground"] = "black"
        sixthItemName["background"] = "#f5ece5"

        # Sec Layer Price
        fourthItemPrice = self.addLabel(text="RM25.00", row=8, column=0, sticky="N")
        fourthItemPrice["font"] = ("Helvetica", 15)
        fourthItemPrice["foreground"] = "black"
        fourthItemPrice["background"] = "#f5ece5"

        fifthItemPrice = self.addLabel(text="RM8.00", row=8, column=1, sticky="N")
        fifthItemPrice["font"] = ("Helvetica", 15)
        fifthItemPrice["foreground"] = "black"
        fifthItemPrice["background"] = "#f5ece5"

        sixthItemPrice = self.addLabel(text="RM35.00", row=8, column=2, sticky="N")
        sixthItemPrice["font"] = ("Helvetica", 15)
        sixthItemPrice["foreground"] = "black"
        sixthItemPrice["background"] = "#f5ece5"

        # Sec Layer Buttons
        self.fourthCartItem = self.addButton(text="Add to cart", row=9, column=0,
                                             command=self.openCatalogNecklace)

        self.fifthCartItem = self.addButton(text="Add to cart", row=9, column=1,
                                            command=self.openCatalogRing)

        self.sixthCartItem = self.addButton(text="Add to cart", row=9, column=2,
                                            command=self.openCatalogWatch)

        #  ====================================== BOTTOM PANEL ======================================

        paymentPanel = self.addPanel(row=10, column=0, columnspan=3, background="#f5ece5")

        # Open to cart window (ByLuxeCart)
        paymentPanel.addButton(text="Payment", row=0, column=0,
                               command=self.openCart)

        # Exit program
        paymentPanel.addButton(text="Exit", row=0, column=1,
                               command=self.exitProgram)

    def openCatalogAnklet(self):
        self.master.destroy()
        catalog_item_window = catalogItem(self.USERNAME)
        catalog_item_window.catalogAnklet()


    def openCatalogBracelet(self):
        self.master.destroy()
        catalog_item_window = catalogItem(self.USERNAME)
        catalog_item_window.catalogBracelet()

    def openCatalogEarring(self):
        self.master.destroy()
        catalog_item_window = catalogItem(self.USERNAME)
        catalog_item_window.catalogEarring()

    def openCatalogNecklace(self):
        self.master.destroy()
        catalog_item_window = catalogItem(self.USERNAME)
        catalog_item_window.catalogNecklace()

    def openCatalogRing(self):
        self.master.destroy()
        catalog_item_window = catalogItem(self.USERNAME)
        catalog_item_window.catalogRing()


    def openCatalogWatch(self):
        self.master.destroy()
        catalog_item_window = catalogItem(self.USERNAME)
        catalog_item_window.catalogWatch()

    def openCart(self):
        from ByLuxeCart import Cart
        self.master.destroy()
        Cart(self.USERNAME)

    def exitProgram(self):
        self.master.destroy()
        # Rating Box
        from CustRating import CustRating
        CustRating()
