n = int(input("Entrer le nombre de nombre"))
d = [input("Entrer un nombre") for i in range(n)]

x = ''.join(d)
y = ''.join(reversed(d))

print(x)
print(y)

print(int(x) + int(y))

