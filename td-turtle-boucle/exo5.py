import turtle as tt

a = 0
tt.speed(0)
for i in range(3):
	tt.setheading(0)
	a += 45
	tt.right(a)
	tt.pensize(1)
	s = 1  # Taille du trait
	while tt.ycor() > -176:  # Faire en sorte que tout les traits s'arrêtent à la même hauteur
		tt.forward(1)
		tt.pensize(s)
		s += 0.1
	tt.up()
	tt.goto(-(i + 1) * 50, 0)
	tt.down()
