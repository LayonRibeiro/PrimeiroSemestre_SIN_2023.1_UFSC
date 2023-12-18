operacao  = input()
matriz = [[float(input()) for i in range(12)] for j in range(12)]
cont = 0
resultado = 0

for i in range(5):
    resultado += sum(matriz[i][1+i:11-i])
    cont += len(matriz[i][1+i:10-i])+1
if operacao == 'S':
    print(f"{resultado:.1f}")
else:
    resultado = round(resultado/cont, 1)
    print(f"{resultado:.1f}")