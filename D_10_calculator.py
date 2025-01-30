print(''' __________
| ________ |
||12345678||
|""""""""""|
|[M|#|C][-]|
|[7|8|9][+]|
|[4|5|6][x]|
|[1|2|3][%]|
|[.|O|:][=]|
"----------" ''')

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

num1 = int(input("What's the first number?: "))

for symbol in oprations:
    print(symbol)

opration_symbol = input("Pick an operation from the line above: ")
num2 = int(input("What's the second number?: "))
calculation_function = oprations[opration_symbol]
first_answer = calculation_function(num1 , num2)

print(f"{num1} {opration_symbol} {num2} = {first_answer}")

opration_symbol = input("Pick an operation from the line above: ")
num3 = int(input("What's the next number? "))
calculation_function = oprations[opration_symbol]
second_answer = calculation_function(calculation_function(num1 , num2) , num3)

print(f"{first_answer} {opration_symbol} {num3} = {second_answer}")

