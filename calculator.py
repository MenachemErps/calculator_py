import sys


def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num2 == 0:
        return "Cannot devide by zero"
    return num1 / num2

def user_math_type(operation):
    if operation == "+":
        return "addition"
    elif operation == "-": 
        return "subtraction"
    elif operation == "*":  
        return "multiply"
    elif operation == "/":  
        return "division"

def operate_calc(x, y, operator):  
    if operator == "addition":
        return addition(x, y)
    elif operator == "subtraction":
       return subtraction(x, y)
    elif operator == "multiply":
        return multiply(x, y)
    elif operator == "division":
        return division(x, y)
    
def get_user_input():
    first_oporand = input("Enter the first number: ")
    if first_oporand == "exit":
        quit()
    try:
        first_oporand = int(first_oporand)
        print(f"first_oporand")
    except ValueError:
        sys.exit("Error! Enter valid numbers")
    
    second_oporand = input("Enter the second number: ")
    if second_oporand == "exit":
        quit()
    try:
        second_oporand = int(second_oporand)
        print(f"second_oporand")
    except ValueError:
        sys.exit("Error! Enter valid numbers")
    
    oporation = input("Enter the operation (+, -, *, /): ")
    if oporation == "exit":
        quit()
    if oporation in ("+", "-", "*", "/"):
        oporation = user_math_type(oporation)
        print(f"oporation {oporation}")
    else:
        print("Invalid operation")
        sys.exit("Invalid operation")
    
    return first_oporand, second_oporand, oporation
    first_oporand, second_oporand, oporation = get_user_input()
    result = operate_calc(first_oporand, second_oporand, oporation)
while True:
    first_oporand, second_oporand, oporation = get_user_input()
    result = operate_calc(first_oporand, second_oporand, oporation) 
    print(f"result: {result}")
