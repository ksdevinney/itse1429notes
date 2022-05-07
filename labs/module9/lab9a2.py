# Lab 9A2
# Katie Devinney
# Uses the employeedata class to track employee data

from employeedata import EmployeeData

def main():
    # create Helen
    h = EmployeeData("Helen Calder", "Analyst", 45000, 5)
    
    # give her a raise
    h.giveRaise(.2)
    
    print(h.getName())

    print(h.getTitle())

    print(h.getSalary())

    # create Fred
    f = EmployeeData("Fred Amaris", "Accountant", 67000, 3)

    f.giveRaise(.15)

    print(f.getName())

    print(f.getTitle())

    print(f.getSalary())

if __name__ == "__main__":
    main()