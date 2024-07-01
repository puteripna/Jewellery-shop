"""
Program   : CustRating.py
Author    : Nur Izzaty binti Yaacob (23039735)
Date      : 27 April 2024

Allows users to rate service by choosing from a combo box.

"""

from breezypythongui import EasyFrame

class CustRating(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title= "Rating", width=480, height=160)
        self.setBackground("#f5ece5")
        self.setResizable(False)

        thxMsg = self.addLabel(text="✿  Thank you for shopping with us!  ✿", \
                               row=0, column=0, sticky="NSEW")
        thxMsg["font"] = ("TIMES", 20)
        thxMsg["foreground"] = "#45523e"
        thxMsg["background"] = "#f5ece5"

        rateMsg = self.addLabel(text="Please rate our services from 1 - 5", \
                               row=1, column=0, sticky="EW")
        rateMsg["font"] = ("TIMES", 20)
        rateMsg["foreground"] = "#45523e"
        rateMsg["background"] = "#f5ece5"

        options = [5, 4, 3, 2, 1]


        self.rateCombo = self.addCombobox(text="", values=options, row=2, column=0, sticky="EW")
        self.ok = self.addButton(text="OK", row=3, column=0, columnspan=3, command=self.close)

    def close(self):
        self.master.destroy()


