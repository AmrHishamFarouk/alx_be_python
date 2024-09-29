no1 = int(input("enter the first number:"))
no2 = int(input("enter the second number:"))
operation = input("Choose the operation (+, -, *, /):")

match operation:
    case "+":
        print("The result is", no1+no2)
    case "-":
        print("The result is", no1-no2)
    case "*":
        print("The result is", no1*no2)
    case "/":
        if no2 == 0:
            print("Cannot divide by zero.")
        else:
            print("The result is", no1/no2)


