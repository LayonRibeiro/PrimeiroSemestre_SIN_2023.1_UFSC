cartas = [int(x) for x in input().split()]

crescente = sorted(cartas)
decrescente = sorted(cartas, reverse = True)

if cartas == crescente:
    print("C")
elif cartas == decrescente:
    print("D")
else:
    print("N")