#!/usr/bin/python3
"""garage module"""

class Garage:
    def __init__(self):
        """python calls the dunder init method for us automatically
        making it a special method
        """
        self.cars = []
    def __len__(self):
        return len(self.cars)

    def __getitem__(self, i):
        return self.cars[i]


ford = Garage()
ford.cars.append("Fiesta")
ford.cars.append("Focus")
print(len(ford)) #reps len(ford.cars)
print(ford[0]) #represents Garage.__getitem__(ford, 0
print(dir(Garage))
print(Garage.__dict__)
print(ford.__dict__)
