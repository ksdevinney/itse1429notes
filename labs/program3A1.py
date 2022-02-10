# Program 3A1
# Katie Devinney
# calculates an employee's pay for the week

payRate = float(input("What is the hourly pay? ")) 
totalHours = float(input("How many hours worked? ")) 

if totalHours > 40:
    regularHours = 40
    overtimeHours = totalHours - regularHours # save overtime hours to a variable
    regularPay = regularHours * payRate # calculate pay for regular hours
    overtimePay = overtimeHours * payRate * 1.5 # calculate overtime pay
    totalPay = overtimePay + regularPay # add regular pay and overtime pay
    print("%.2f" % regularHours + " regular and %.2f" % overtimeHours + " overtime at %.2f" % payRate + " = %.2f" % totalPay) # print output
else:
    regularHours = totalHours
    totalPay = regularHours * payRate # calculate pay for regularhours
    print("%.2f" % regularHours + " regular at %.2f" % payRate + " = %.2f" % totalPay) # print output