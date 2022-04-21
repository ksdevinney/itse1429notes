# Lab 8A3
# Katie Devinney
# Calculates the cost of renting a moving truck

from breezypythongui import EasyFrame

class MovingTruck(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self)
        self.addLabel(text = "Enter the number of miles and hours below.", row = 0, column = 0)
        self.setTitle("Cost of a Moving Truck")

        # input fields
        self.addLabel(text = "Hours", row = 1, column = 0)
        self.hoursBox = self.addIntegerField(value = 0, row = 1, column = 1)

        self.addLabel(text = "Miles", row = 2, column = 0)
        self.milesBox = self.addIntegerField(value = 0, row = 2, column = 1)

        # button
        self.addButton(text = "Calculate", row = 3, column = 1, command = self.cost)

        # output
        self.addLabel(text = "Total Cost", row = 4, column = 0)
        self.outputField = self.addFloatField(value = 0.00, row = 4, column = 1, precision= 2)

    def cost(self):
        hours = self.hoursBox.getNumber()
        miles = self.milesBox.getNumber()

        rentalCost = 200

        if miles < 0 or hours < 0:
            self.messageBox(title = "ERROR", message = "Input must be a positive number")
        else:
            rentalCost = 200 + (150 * hours) + (2 * miles)

        self.outputField.setNumber(rentalCost)

def main():
    MovingTruck().mainloop()

if __name__ == "__main__":
    main()