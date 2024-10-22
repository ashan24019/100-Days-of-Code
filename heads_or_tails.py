import random

names_string = input("Give me everybody's names,seperated by a comma:-")

names = names_string.split(",")

print(names)

random_number = random.randint(0,len(names)-1)

print(f"{names[random_number]} has to pay the whole bill") 