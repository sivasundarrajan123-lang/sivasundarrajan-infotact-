import math
import os

name = "Siva"
age = 22


class Student:
    def __init__(self):
        self.name = name

    def study(self):
        print("Studying...")


def greet():
    print("Hello, Welcome to PyChronicle!")


for i in range(3):
    greet()


while age < 23:
    age += 1


if age >= 23:
    greet()


print(math.sqrt(25))