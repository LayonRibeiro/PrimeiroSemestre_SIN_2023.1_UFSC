qntd_linhas, qntd_colunas, p0 = [int(x) for x in input().split()]
matriz = []

for i in range(linhas):
    linha = []
    for j in range(colunas):
        x= int(input())
        linha.append(x)
    matriz.append(linha)