#!/usr/bin/python3
"""
oop practice module
using .__str instead of description instance method
"""

class Dog:
    species  = "Canis familiaris"
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        """
        Returns:
            string displaying the name and age of the dog
        this is an instance method and its first parameter is self
        """
        return f"{self.name} is {self.age} years old"
    
    def speak(self, sound):
        """
        Args:self, sound
        Returns:
            string containing the dog's name and the sound it makes
        """
        return f"{self.name} says {sound}"
miles = Dog("Miles", 4)
# print(miles.description())
# print(miles.speak("Woof Woof"))
print(miles)
