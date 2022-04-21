# Lab 8A1
# Katie Devinney
# Converts miles to kilometers

from breezypythongui import EasyFrame

class MilesConverter(EasyFrame):

    def __init__(self):
        # window setup
        EasyFrame.__init__(self)
        self.addLabel(text = "Enter the number of miles below.", row = 0, column = 0)
        self.setSize(400, 250)
        self.setTitle("Distance Converter")

        # widgets for miles
        self.addLabel(text = "Miles", row = 1, column = 0)
        self.inputField = self.addFloatField(value = 0, row = 1, column = 1)

        # widgets for km
        self.addLabel(text = "Kilometers", row = 2, column = 0)
        self.outputField = self.addFloatField(value = 0, row = 2, column = 1, precision= 2)

        # button
        self.addButton(text = "Convert", row = 3, column = 0, command = self.convert)

        # enter button functionality
        self.inputField.bind("<Return>", lambda event: self.convert())

    # conversion function
    def convert(self):
        miles = self.inputField.getNumber()

        # not sure if I really need this since it wouldn't raise an exception
        if miles < 0:
            self.messageBox(title = "ERROR", message = "Input must be a positive number")
        else:
            km = 1.60934 * miles
            self.outputField.setNumber(km)

def main():
    MilesConverter().mainloop()


if __name__ == "__main__":
    main()