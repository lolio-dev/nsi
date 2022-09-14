grades_nb = int(input("Entrer le nombre de note"))
grades = [int(input(f"Entrer la note n°{i + 1}")) for i in range(grades_nb)]

print(f'Moyenne: {sum(grades) / grades_nb}')