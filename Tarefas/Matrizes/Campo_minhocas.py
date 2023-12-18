lin, col = [int(x) for x in input().split()]
matriz = [[int(x) for x in input().split()] for _ in range(lin)]
maior = 0

# linhas
for i in range(lin):
    if maior < sum(matriz[i]):
        maior = sum(matriz[i])

for j in range(col):
    soma = 0
    for i in range(lin):
        soma += matriz[i][j]
    if soma > maior:
        maior = soma

print(maior)