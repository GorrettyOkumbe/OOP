#!/usr/bin/python3
"""inheritance and use of super()"""

class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} barks: {sound}"


class GoldenRetriever(Dog):
    def speak(self, sound="Bark"):
        return super().speak(sound)


buddy = GoldenRetriever("Buddy", 7)
print(buddy)
print(buddy.speak())


