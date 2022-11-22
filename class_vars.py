#!/usr/bin/python3
"""class vars module"""

class Variables:
    Humans  = "Africans"
    def __init__(self,name,country):
        self.name = name
        self.country = country

    # def __str__(self):
        # return f"{self.name} is from {self.country}"
    def __repr__(self):
        return f"<<{self.name}>> => {self.country}"

hum1 = Variables("Careen", "Kenya")
hum2 = Variables("Ronny", "Ghana")
print(hum1.Humans == hum2.Humans)
print(hum1 == hum2)
print(hum1)
print(eval(repr))
