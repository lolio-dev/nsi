"""
auteurs: Antoine Grolleau & Elie Pernet
Le programme marche pour side_lenght > 20 soit nmax = f(x) ->
"""

import turtle as t
from math import degrees, asin, sqrt

t.speed(0)
side_lenght = 250
n = int(input('Entrer le nombre d\'itération'))


def get_delta(a: int, b: int, c: int) -> int:
	"""
	Retourne le discriminant d'une équation de type ax² + bx + c = 0
	Args:
		c (int): Constante a de l'équation
		b (int): Constante b de l'équation
		a (int):  Constante c de l'équation

	Returns:
		int: Discriminant delta
	"""
	return b ** 2 - 4 * a * c


def get_gap_lenght(l1: int, l2: int) -> float:
	"""
	Retoune
	Args:
		l1 (int): Valeur initial d'une arrête du carré
		l2 (int): Valeur d'une arrête du carré pour l'itération suivante

	Returns:
		float: La valeur de x1 de l'équation ax² + bx + c = 0
	"""
	a, b, c = 2, 2 * l1, l1 ** 2 - l2 ** 2
	delta = get_delta(a, b, c)

	try:
		return (b - sqrt(delta)) / (2 * a)
	except ValueError:
		return 0


def get_angle(opposite_side_lenght: float, hypo_lenght: int) -> float:
	"""
	Args:
		opposite_side_lenght: Taille de l'écart entre l'itération actuel et la suivante défini par get_gap_lenght
		hypo_lenght: Valeur d'une arrête du carré pour l'itération suivante

	Returns:
		float: l'angle pour que hypo_lenght soit à la bonne taille
	"""
	return degrees(asin(opposite_side_lenght / hypo_lenght))


def square() -> None:
	"""
	Dessine un carré
	Returns: None
	"""
	for _ in range(4):
		t.forward(side_lenght)
		t.right(90)


for _ in range(n):
	square()
	gap = get_gap_lenght(side_lenght, side_lenght - 10)

	if gap == 0:
		print("Impossible, discriminant < 0")
		break

	t.forward(gap)
	side_lenght -= 10
	t.right(get_angle(gap, side_lenght))

t.mainloop()
