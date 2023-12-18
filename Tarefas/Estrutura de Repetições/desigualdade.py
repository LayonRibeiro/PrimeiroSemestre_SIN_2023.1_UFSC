import math
n = 1

while (math.factorial(n) <= (n**10)):
    n += 1

print(n,"elevado a 10 é:",n**10)
print("fatorial de",n, "é:",math.factorial(n))