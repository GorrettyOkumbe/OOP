#!/usr/bin/python3
"""oop practice module"""

class Dog:
    species  = "Canis familiaris"
    def __init__(self, name, age):
        self.name = name
        self.age = age
buddy = Dog("Buddy", 9)
miles = Dog("Miles", 4)
# miles.species = "Felis Silvestris"
print(buddy.name, buddy.age)
print(buddy.species)
print(miles.name, miles.age)
print(miles.species)
