height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

BMI = round(weight/height**2)

if BMI < 18.5:
    print(f"your BMI is {BMI},You are under weight")
elif BMI < 25:
    print(f"your BMI is {BMI},You are normal weight")
elif BMI < 30:
    print(f"your BMI is {BMI},You are overweight")
elif BMI < 35:
    print(f"your BMI is {BMI},You are obese")
else: print(f"your BMI is {BMI},You are clinically obese")