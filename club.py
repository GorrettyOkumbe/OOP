#!/usr/bin/python3
"""club module"""

class Club:
    def __init__(self, name):
        """constructor method"""
        self.name = name
        self.players = []

    def __getitem__(self, i):
        return self.players[i]

    def __len__(self):
        return len(self.players)

    def __repr__(self):
        return f"Club {self.name}: {self.players}"

    def __str__(self):
        return f"Club {self.name} with {len(self.players)} players"


my_club = Club("Arsenal")
my_club.players.append("Rolf")
my_club.players.append("Anne")
print(my_club)

