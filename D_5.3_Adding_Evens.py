total_of_evens = 0
for number in range(0,101,2):
    total_of_evens += number

total_of_evens2 = 0
for number in range(0 , 101):
    if number % 2 == 0 :
        total_of_evens2 += number

    

print(f"Total of even numbers 1 to 100={total_of_evens}")
print(f"Total of even numbers 1 to 100={total_of_evens2}")