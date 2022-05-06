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
        return "Name: %s" % self.name

    def getTitle(self):
        return "Title: %s" % self.title
    
    def getSalary(self):
        return "Salary: %0.2f" % self.salary

    def getExpYears(self):
        return "Years of Experience: %d" % self.exp

    def giveRaise(self, percent):
        self.salary = self.salary * (1 + percent)

    def __str__(self):
        # returns employee data with labels
        return "Name: %s\nTitle: %s\nSalary: %0.2f\nYears of Experience: %d" % (self.name, self.title, self.salary, self.exp)