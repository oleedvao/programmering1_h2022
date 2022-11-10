from random import randint


class Die:
	def __init__(self, sides=6):
		self.sides = sides

	def roll_die(self):
		return randint(1, self.sides)

	def roll_dice(self, number_of_times):
		print(f"Rolling d{self.sides} {number_of_times} times: ")
		for i in range(number_of_times):
			print(self.roll_die())


# Funksjonen fungerer uavhengig av klassen, men krever et "die"-objekt
# Funksjonen får alt den trenger som parametere
def roll_dice(die, number_of_times):
	print(f"Rolling d{die.sides} {number_of_times} times: ")
	for i in range(number_of_times):
		print(die.roll_die())

d6 = Die()
# Metodekall med d6-objektet
d6.roll_dice(10)

d10 = Die(10)
# Funksjonskall, hvor vi sender d10 objektet inn som parameter
roll_dice(d10, 10)

d20 = Die(20)
roll_dice(d20, 100)