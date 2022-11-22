#!/usr/bin/python3
"""
oop practice module
creates child classes representing different breeds
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



class JackRussellTerrier(Dog):
    def speak(self, sound="Arf"):
        return super().speak(sound)


class Dachshund(Dog):
    pass

class Bulldog(Dog):
    pass

miles = JackRussellTerrier("Miles", 4)
buddy = Dachshund("Buddy", 9)
jack = Bulldog("Jack", 3)
jim = Bulldog("Jim", 5)
print(miles.speak())
