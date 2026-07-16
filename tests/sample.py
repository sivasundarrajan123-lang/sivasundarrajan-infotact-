import os
import math

name = "Siva"
age = 22

class Student:
    def __init__(self):
        self.name = name

def greet():
    print("Hello")

for i in range(3):
    greet()

while age < 25:
    age += 1

if age >= 18:
    greet()