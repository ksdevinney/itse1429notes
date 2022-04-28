# Lab 8B1
# Katie Devinney
# Converts a temperature in farenheit to celsius

from breezypythongui import EasyFrame

class TempConverter(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, "Temperature Converter")
        self.addLabel(text = "Enter the temperature, in Farenheit", row = 0, column = 0)

        # input for F
        self.addLabel(text = "Farenheit", row = 1, column = 0)
        self.inputField = self.addFloatField(value = 0, row = 1, column = 1)
        
        # radio buttons
        # self.unitSelector = self.addRadiobuttonGroup(row = 1, column = 2)
        # defaultRB = self.unitSelector.addRadiobutton(text = "Farenheit")
        # self.unitSelector.setSelectedButton(defaultRB)
        # self.unitSelector.addRadiobutton(text = "Celsius")

        # output for C
        self.addLabel(text = "Celsius", row = 2, column = 0)
        self.outputField = self.addFloatField(value = 0, row = 2, column = 1, precision = 1)

        # button
        self.addButton(text = "Convert", row = 3, column = 0, command = self.convert)

        self.inputField.bind("<Return>", lambda event: self.convert())

    def convert(self):
        far = self.inputField.getNumber()

        cels = (far - 32) * (5/9)
        self.outputField.setNumber(cels)

def main():
    TempConverter().mainloop()

if __name__ == "__main__":
    main()