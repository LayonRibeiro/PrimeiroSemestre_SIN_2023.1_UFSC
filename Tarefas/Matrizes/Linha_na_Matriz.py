matriz = []
ref = int(input())
operacao  = input()

for i in range(12):
    linhas = []
    for j in range(12):
        linhas.append(float(input()))
    matriz.append(linhas)

if operacao == 'S' :
    resultado = sum(matriz[ref])
else:
    resultado = (sum(matriz[ref]))/12
    
print(f'{resultado:.1f}')