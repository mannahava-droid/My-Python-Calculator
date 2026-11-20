print("==============================")
print("       MY CALCULATOR")
print("==============================")

while True:
    print("\nSelect an operation:")
    print("+  Addition")
    print("-  Subtraction")
    print("*  Multiplication")
    print("/  Division")
    print("q  Exit")
    choice = input("\nPick karein (+, -, *, / ya q): ")
    if choice == "q":
        print("Thank you!")
        break
    if choice not in ["+", "-", "*", "/"]:
        print("Invalid choice!")
        continue
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if choice == "+":
            print("Result:", num1 + num2)
        elif choice == "-":
            print("Result:", num1 - num2)
        elif choice == "*":
            print("Result:", num1 * num2)
        elif choice == "/":
            if num2 == 0:
                print("Error! Cannot divide by zero.")
            else:
                print("Result:", num1 / num2)
    except ValueError:
        print("Please enter valid numbers!")