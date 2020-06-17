def add(x, y):
    return x+y

def subtract(x, y):
    return x-y

def multiply(x, y):
    return x*y

def divide(x, y):
    return x/y

print(" Welcom to Tandemloop Simple Calculator.")

while True:
   operation = input("Enter operation(add subtract divide multiply): ")
   if operation in ('add', 'subtract', 'divide', ''multiply'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if operation == 'add':
            print(num1 + num2)

        elif operation == 'subtract':
            print(num1 - num2)

        elif operation == 'multiply':
            print(num1 * num2)

        elif operation == 'divide':
            print(num1 / num2)
        break
    else:
        print("Invalid Input")
