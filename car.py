#!/usr/bin/python3
"""car class module"""

class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __str__(self):
        return f"The {self.color} car has {self.mileage:,} miles."

red_car = Car("red", 30000)
blue_car = Car("blue", 20000)

print(red_car)
print(blue_car)
