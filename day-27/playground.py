from mimetypes import inited


def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum


# print(add(3, 5, 9))

def calculate(n, **kwargs):
    print(kwargs)

    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(6, add = 5, multiply=8)

class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")


my_car = Car(make="Nissan", model="GT-R")
print(my_car.model)