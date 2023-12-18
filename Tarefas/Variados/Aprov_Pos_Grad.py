x1, x2, x3, x4 = [str(w) for w in input().split()]
i = 1
lista_conceitos = ["excelente","bom","satisfatório","insuficeinete"]

for i in range(lista_conceitos[1],lista_conceitos[i],1):
    if x1 or x2 or x3 or x4 == lista_conceitos[i]:
        x1 = lista_conceitos[i]

print(x1)
ia =(x1+x2+x3+x4)/4