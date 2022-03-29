"""
Program 6A2
Katie Devinney

"""

def addDigits(x):
    # length = len(x)
    sum = 0

    for i in range(0, 5):
        x[i] = int(x[i])
        sum += x[i]

    # print(sum)
    return sum

def main():
    file = open("lab6A2.txt", 'r')

    numbers = file.read()
    numbers = numbers.split()

    for i in range(0, len(numbers)):
        print("The number is %d" % i)
        addDigits(i)
        print("The sum of its digits is %d" % i)

if __name__ == "__main__":
    main()