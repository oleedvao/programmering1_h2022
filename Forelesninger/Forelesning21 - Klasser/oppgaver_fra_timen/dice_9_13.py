from random import randint


class Die:

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(randint(1, self.sides))

    def roll_dice(self, number_of_times):
        print(f"\nWe roll the d{self.sides} {number_of_times} times:")
        for roll_number in range(number_of_times):
            self.roll_die()


d6 = Die()
d6.roll_dice(3)

d10 = Die(10)
d10.roll_dice(3)

d20 = Die(20)
d20.roll_dice(4)