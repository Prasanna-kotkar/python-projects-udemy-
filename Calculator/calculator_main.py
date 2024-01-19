
from calculator_art import logo

def add(a,b):
    return a + b
def sub(a,b):
    return a - b
def mul(a,b):
    return a * b
def div(a,b):
    return a / b

opration = {
    "+" : add,
    "-" : sub,
    "*" : mul,
    "/" : div,
}
print(logo)
def calculator():
    num1 = float(input("Enter the first number: "))
    for i in opration:
        print(i)
    while True:
        choice = input("Pick an operation: ")
        if choice not in opration:
            print("!!! INVALID OPERATION. !!!")
        else:
            num2 = float(input("Enter the second number: "))
            func = opration[choice]
            num3 = func(num1,num2)
            print(f"{num1} {choice} {num2} = {num3}")
            ch = input(f'Type "y" to continue clculating with {num3} or "n" to start a new calculation: ').lower()
            if ch == "y":
                num1 = num3
            else:
                calculator()

calculator()