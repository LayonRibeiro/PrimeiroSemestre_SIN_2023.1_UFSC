linhas, colunas = [int(x) for x in input().split()]
matriz = [[int(x) for x in input().split()] for _ in range(linhas)]

x , y = [int(x) for x in input().split()]
x -= 1
y -= 1
soma = 0
cont = 0

for l in range(linhas):
    for c in range(colunas):
        a = abs(x - l)
        b = abs(y - c)
        if max(a,b) == 1:
            soma += matriz[l][c]
            cont += 1
    
            
print(f"{soma/cont:.1f}")