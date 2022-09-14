from math import prod

print(' * '.join(str(i + 1) for i in range(100)) + " = " + str(prod([i for i in range(1, 101)])))