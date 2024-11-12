import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',]

numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!' , '#','$','%','$' , '(',')','*','+']
print("Welcome to the password generator!")
nr_letters = int(input("How many letterss would you like in your password?\n"))

nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_list = []

for letter in range(0 , nr_letters + 1):
    random_letters = random.choice(letters)
    password_list += random_letters

for symbol in range(0 , nr_symbols + 1):
    random_symbols = random.choice(symbols)
    password_list += random_symbols


for number in range(0 , nr_numbers + 1):
    random_numbers = random.choice(numbers)
    password_list += random_numbers


random.shuffle(password_list)

password = ""

for n in password_list:
    password += n
print(f"Your pass word is:{password}") 