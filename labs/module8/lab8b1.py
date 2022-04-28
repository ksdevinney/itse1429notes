# Lab 8B1
# Katie Devinney
# Converts a temperature in Fahrenheit to celsius, or vice versa

from breezypythongui import EasyFrame

class TempConverter(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, "Temperature Converter")
        self.addLabel(text = "Enter the temperature in Fahrenheit, or check the box for Celsius.", row = 0, column = 0)

        # input for F
        self.addLabel(text = "Fahrenheit", row = 1, column = 0)
        self.inputField = self.addFloatField(value = 0, row = 1, column = 1)
        
        """
        I really wanted this to be radio buttons instead, but got an error from breezypythongui every time I tried to run it.
        There was a possible solution posted online, but I didn't want to mess with the library.
        A check box seemed to be the only solution...
        """
        self.checkForCels = self.addCheckbutton(text = "Celsius", row = 1, column = 2)

        # button
        self.addButton(text = "Convert", row = 2, column = 0, command = self.convert)

        # output boxes
        self.addLabel(text = "Celsius", row = 3, column = 0)
        self.celsOut = self.addFloatField(value = 0, row = 3, column = 1, precision = 1)

        self.addLabel(text = "Fahrenheit", row = 4, column = 0)
        self.farOut = self.addFloatField(value = 0, row = 4, column = 1, precision = 1)

        self.inputField.bind("<Return>", lambda event: self.convert())

    def convert(self):
        tempIn = self.inputField.getNumber()

        if self.checkForCels.isChecked():
            tempOut = (tempIn * (9/5)) + 32
            self.farOut.setNumber(tempOut)
            self.celsOut.setNumber(tempIn)
            
        else:
            tempOut = (tempIn - 32) * (5/9)
            self.celsOut.setNumber(tempOut)
            self.farOut.setNumber(tempIn)

def main():
    TempConverter().mainloop()

if __name__ == "__main__":
    main()