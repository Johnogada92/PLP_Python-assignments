#1. ask the user to use the first number
num1 = float(input("Enter yur first number: "))

#2. ask the user to input the second number
num2 = float(input("Enter you second number: "))

#3. ask the user to input an operational symbol
operation = input("Enter and operator(+,-,*,/,%): ")

#4. use if, elif and else to perform the operation
if operation == "+":
        result = num1 + num2
        print(f"{num1}+{num2}={result}")
elif operation == "-":
        result = num1 - num2
    print(f"{num1}-{num2}={result}")
elif operation == "*":
        result = num1 * num2
    print(f"{num1}*{num2}={result}")
elif operation == "%":
        result = num1 % num2
    print(f"{num1}%{num2}={result}")
elif operation == "/":
    if num2 !=0:
        result = num1 / num2
        print(f"{num1}/{num2}={result}")
    else:
        print("Error: Cannot be divedied by zero")
else:
    A
 print("Invalid operation please use")
 quit()
