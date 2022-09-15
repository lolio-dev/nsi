nb = int(input("Entrer le nombre de fin"))

print(' + '.join(str(i) for i in range(1, nb + 1)) + " = " + str(sum(([i for i in range(1, nb + 1)]))))
print(nb * (nb + 1)//2)
# On obtient le même nombre