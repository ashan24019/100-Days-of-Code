import math

def paint_calc(height , width , cover):
    area= height * width
    num_of_cans = math.ceil(area/coverage)
    print(f"You will need {num_of_cans} cans of paints")

test_h = int(input("Hight of wall : "))
test_w = int(input("Width of wall : "))
coverage = 5

paint_calc(height = test_h , width = test_w , cover = coverage )