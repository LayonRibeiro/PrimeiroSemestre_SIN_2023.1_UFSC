c1 = [int(x) for x in input().split()]
c2 = [int(x) for x in input().split()]

saida = "Y"

for i in range(len(c1)):
    if c1[i] == c2[i]:
        saida = "N"
        break

print(saida)