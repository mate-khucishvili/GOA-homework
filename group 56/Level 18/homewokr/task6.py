# Program to perform basic arithmetic operations

# Input: Ask the user to enter two numbers and an operator
num1 = float(input("Enter the  number: "))
num2 = float(input("Enter the  number: "))
operator = input("Enter the operator (+, -, *, /): ")

# Perform the calculation based on the operator
if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print = (num1 * num2)
elif operator == "/":
    if num2 != 0:
        print(num1 / num2)
    else:
        print("Eror.")
else:
    print("wrong operator.") 

# Display the result
print("God work")
