import art

def add(n1 , n2):
    return n1 + n2


def subtract(n1 , n2):
    return n1 - n2

def multiply(n1 , n2):
    return n1 * n2

def divide(n1 , n2):
    return n1 / n2

oprations = {
    "+": add ,
    "-": subtract ,
    "*": multiply ,
    "/": divide
}

def calculator():
    print(art.text2art("Calculator"))

    num1 = float(input("What's the first number?: "))

    for symbol in oprations:
        print(symbol)

    should_continue = True

    while should_continue:

        opration_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = oprations[opration_symbol]
        answer = calculation_function(num1 , num2)

        print(f"{num1} {opration_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer} or type 'n' to start new calculation.") == "y":
            num1 = answer
        
        else: 
            should_continue = False
            calculator()
        

calculator()






