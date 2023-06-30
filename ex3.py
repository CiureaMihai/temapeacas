try:

    num1 = float(input("Enter the first number: "))


    num2 = float(input("Enter the second number: "))


    result = num1 / num2

    # Print the result
    print("The result of the division is:", result)

except ZeroDivisionError:

    print("Error: Division by zero is not allowed.")