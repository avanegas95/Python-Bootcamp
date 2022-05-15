#Calculator
from art import logo

#Add
from timeit import repeat


def add(n1,n2):
    return n1 + n2

#Subtract
def subtract(n1,n2):
    return n1 - n2

#Multiply
def multiply(n1,n2):
    return n1 * n2

#Divide
def divide(n1,n2):
    return n1 / n2

operations = {
    "+": add, 
    "-": subtract, 
    "*": multiply, 
    "/": divide
    }

def calculator():
    print(logo)
    num1 = float(input("What is the first number?: "))
    continue_calculating = True

    while continue_calculating:
        for key in operations:
            print(key)
        operation_symbol = input("Pick an operation from the line above: ")
        num2 = float(input("What is the next number?: "))
        answer = operations[operation_symbol](num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
            continue_calculating = True
            num1= answer
        else:
            continue_calculating = False
            calculator()

calculator()