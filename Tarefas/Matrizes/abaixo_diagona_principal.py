operacao  = input()
matriz = [[float(x) for x in input().split()] for _ in range(12)]
cont = 0

for i in range(12):
    for j in range(12):
        if i > j:
            resultado += matriz[i][j]
            cont += 1
if operacao == 'S':
    print(resultado)
else:
    print(resultado/cont)