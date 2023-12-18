notas = [float(x) for x in input().split()]
notas.sort()
nota_final = sum(notas[1:4])
print(f"{nota_final:.1f}")