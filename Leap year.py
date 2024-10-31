year = int(input("Enter a year: ")) 

if year % 400 == 0 :
    print(f"{year} is a Leap year")

elif year % 100 == 0 :
    print(f"{year} is not a Leap year")

elif year % 4 == 0 :
    print(f"{year} is a Leap year")

else : print(f"{year} is a not a Leap year")