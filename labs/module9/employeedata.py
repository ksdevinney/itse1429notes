# employeedata
# Katie Devinney
# manages an employee and data such as name, title, salary, and years of experience

class EmployeeData(object):

    def __init__(self, name, title, salary, exp):
        self.name = name
        self.title = title
        self.salary = salary
        self.exp = exp

    def getName(self):
        return "Name: " + self.name

    def getTitle(self):
        return "Title: " + self.title
    
    def getSalary(self):
        return "Salary: " + str(self.salary)

    def getExpYears(self):
        return "Years of Experience: " + str(self.exp)

    def giveRaise(self, percent):
        self.salary = self.salary * (1 + percent)
        # return str(self.salary)

    def __str__(self):
        # returns employee data with labels
        return "Name: " + self.name + "\nTitle: " + self.title + "\nSalary: " + str(self.salary) + "\nYears of Experience: " + str(self.exp)