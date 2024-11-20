def prime_checker(number):
    if number == 2 :
        print(f"{number} is a even number")

    elif number % 2 == 0:
        print(f"{number} is a even number")
    
    else:
        print(f"{number} is a prime number")
    

n = int(input("Check this number: "))

prime_checker(number=n)