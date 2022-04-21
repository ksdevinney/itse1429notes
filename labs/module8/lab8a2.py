# Lab 8A2
# Katie Devinney
# takes in an money amount (in cents) and ouputs how many coins of each denomination it is equal to

from breezypythongui import EasyFrame

class SpareChange(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self)
        self.addLabel(text = "Enter the amount of money, in cents, and press the button.", row = 0, column = 0)
        self.setTitle("Change Machine")

        # input money amount
        self.addLabel(text = "Amount", row = 1, column = 0)
        self.inputField = self.addIntegerField(value = 0, row = 1, column = 1)

        # button
        self.addButton(text = "Convert", row = 2, column = 0, command = self.convert)

        # output fields
        self.addLabel(text = "Quarters", row = 3, column = 0)
        self.quarterField = self.addIntegerField(value = 0, row = 3, column = 1)

        self.addLabel(text = "Dimes", row = 4, column = 0)
        self.dimeField = self.addIntegerField(value = 0, row = 4, column = 1)

        self.addLabel(text = "Nickels", row = 5, column = 0)
        self.nickelField = self.addIntegerField(value = 0, row = 5, column = 1)

        self.addLabel(text = "Pennies", row = 6, column = 0)
        self.pennyField = self.addIntegerField(value = 0, row = 6, column = 1)

    # convert to coins
    def convert(self):
        money = self.inputField.getNumber()

        quarters = 0
        dimes = 0
        nickels = 0
        pennies = 0

        if money < 0:
            self.messageBox(title = "ERROR", message = "Input must be a positive number")
        
        # keep going until out of change
        while money > 0:
            # find out how many quarters
            if money >= 25:
                money -= 25
                quarters += 1
            # dimes
            elif money >= 10 and money < 25:
                money -= 10
                dimes += 1
            # nickels
            elif money >= 5 and money < 10:
                money -= 5
                nickels += 1
            # pennies
            else:
                money -= 1
                pennies += 1

        self.quarterField.setNumber(quarters)
        self.dimeField.setNumber(dimes)
        self.nickelField.setNumber(nickels)
        self.pennyField.setNumber(pennies)

def main():
    SpareChange().mainloop()


if __name__ == "__main__":
    main()