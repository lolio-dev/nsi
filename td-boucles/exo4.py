initial_sum = int(input("Entrer le somme initial"))
rate = float(input("Entrer le taux annuel"))
years = int(input('Entrer le nombre d\'année'))

total = 0

for i in range(years):
    total += initial_sum * rate / 100
    print(f'année {i + 1}: {total}')

print(total + initial_sum)