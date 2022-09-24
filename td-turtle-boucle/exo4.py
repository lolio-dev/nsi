import turtle as tt

n = int(input("Entrer le nombre de niveaux de gris"))
tt.goto(0, 0)

for i in range(1, n + 1):
	color = i / n
	tt.fillcolor(color, color, color)
	tt.pencolor(color, color, color)
	tt.begin_fill()
	for _ in range(2):
		tt.forward(50)
		tt.right(90)
		tt.forward(200)
		tt.right(90)
	tt.goto(i * 50, 0)
	tt.end_fill()
