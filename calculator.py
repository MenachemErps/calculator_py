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

def user_math_type():
    operation = input("Enter type of math operation \t(1 for addition \n\t\t\t\t 2 for subtraction \n\t\t\t\t 3 for multiplication \n\t\t\t\t 4 for division)\n ")
    if operation in ["1", "2", "3", "4"]:
        return int(operation)
    else:
        raise TypeError("Only numbers one to four (including four)")

def operate_calc():
    try:
        x_str = input("enter first number: ")
        if x_str == "exit":
            return x_str
        operator = user_math_type()
        y_str = input("enter second number: ")
        x = int(x_str)
        y = int(y_str)
        
        if operator == 1:
            return addition(x, y)
        elif operator == 2:
           return subtraction(x, y)
        elif operator == 3:
            return multiply(x, y)
        elif operator == 4:
            return division(x, y)
    except ValueError:
        return "Error! Enter valid numbers"
    except Exception as e:
        return f"something went wrong {e}"

call = 1
while call > 0:
    result = operate_calc()
    if result == "exit":
        break
    print(f"result: {result}")