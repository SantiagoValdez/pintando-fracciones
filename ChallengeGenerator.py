import random

WHITE = 0
RED = 1
GREEN = 2
BLUE = 3
BROWN = 4
PURPLE = 5
YELLOW = 6
PINK = 7
ORANGE = 8
GRAY = 9

COLORS = [WHITE, RED, GREEN, BLUE, BROWN, PURPLE, YELLOW, PINK, ORANGE, GRAY]

class ColoredFraction():
	def __init__(self, numerator, denominator, color):
		self._numerator = numerator
		self._denominator = denominator
		self._color = color

	def get_numerator(self):
		return self._numerator

	def get_denominator(self):
		return self._denominator
	
	def get_color(self):
		return self._color

	def __str__(self):
		return str(self._numerator) + "/" + str(self._denominator) + " : " + str(self._color)

def general(amount_of_fractions, denominator):
	numerators_list = range(1, denominator)
	fractions = []
	numerators = []

	while (sum(numerators) != denominator):
		numerators = []
		for i in range(amount_of_fractions):
			numerators.append(random.choice(numerators_list))

	colors = [c for c in COLORS]

	for numerator in numerators:
		color = random.choice(colors)
		colors.remove(color)
		fraction = ColoredFraction(numerator, denominator, color)
		fractions.append(fraction)

	return fractions

def easy(amount_of_fractions):
	fractions = []

	colors = [c for c in COLORS]

	for i in range(amount_of_fractions):
		color = random.choice(colors)
		colors.remove(color)
		fraction = ColoredFraction(1,amount_of_fractions, color)
		fractions.append(fraction)

	return fractions

print "General"
fracciones = general(9,10)
for f in fracciones:
	print f

print "Facil"
fracciones = easy(5)
for f in fracciones:
	print f
