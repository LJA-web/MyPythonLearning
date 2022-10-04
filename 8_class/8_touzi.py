# 9-14
from random import randint

class Die():
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(randint(1, self.sides))

print("tenSidesDie:")
tenSidesDie = Die(10)
for i in range(0, 10):
    tenSidesDie.roll_die()

print("twentySidesDie:")
twentySidesDie = Die(20)
for i in range(0, 10):
    twentySidesDie.roll_die()