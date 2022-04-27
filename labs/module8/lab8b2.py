# Lab 8B2
# Katie Devinney
# Calculates a test grade based on the total amount of questions and questions missed

from breezypythongui import EasyFrame

class GradeCalculator(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self)
        self.addLabel(text = "Enter the information below.", row = 0, column = 0)
        self.setTitle("Grade Calculator")

        # total questions
        self.addLabel(text = "Total Questions", row = 1, column = 0)
        self.totalQ = self.addIntegerField(value = 0, row = 1, column = 1)

        # missed questions
        self.addLabel(text = "Questions Missed", row = 2, column = 0)
        self.missedQ = self.addIntegerField(value = 0, row = 2, column = 1)

        # button
        self.addButton(text = "Calculate", row = 3, column = 0, columnspan = 3, command = self.gradeTest)

        # grade
        self.addLabel(text = "Your Grade", row = 4, column = 0)
        self.finalGrade = self.addFloatField(value = 0, row = 4, column = 1, precision = 2)

        self.missedQ.bind("<Return>", lambda event: self.gradeTest())

    def gradeTest(self):
        total = self.totalQ.getNumber()

        missed = self.missedQ.getNumber()

        grade = (total - missed) / total * 100

        self.finalGrade.setNumber(grade)
    
def main():
    GradeCalculator().mainloop()

if __name__ == "__main__":
    main()