import os

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

operations_dict={
    '+' : add,
    '-' : sub,
    '*' : mul,
    '/' : div
}
def M_calculator():
    number1 = float(input("Enter first number: "))
    for symbol in operations_dict:
        print(symbol)
    continue_flag = True
    while continue_flag:        
        op_symbol = input("Pick an operator: ")
        number2 = float(input("Enter next number: "))
        calculator_function= operations_dict[op_symbol]
        output = calculator_function(number1, number2)
        print(f"{number1} {op_symbol} {number2} = {output}")
        should_continue=input(f"Enter 'y' to continue calculation with {output} or 'n' to start a new calculation or 'x' to exit: ").lower()
        if should_continue == 'y':
            number1 = output
        elif should_continue == 'n':
            continue_flag = False
            os.system('cls') #This will clear previous output in cosole screen 
            M_calculator()
        elif should_continue == 'x':
            continue_flag = False
            print("Bye")
M_calculator()

