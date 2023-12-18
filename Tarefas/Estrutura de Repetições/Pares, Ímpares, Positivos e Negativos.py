n_pares = 0
n_impares = 0
n_positivos = 0
n_negativos = 0

for i in range(5):
    num = float(input())
    if (num%2 == 0):
        n_pares += 1
    else:
        n_impares += 1
    if num>0:
        n_positivos += 1
    elif num<0:
        n_negativos += 1

print (n_pares,"valor(es) par(es)")
print (n_impares,"valor(es) impar(es)")
print (n_positivos,"valor(es) positivo(s)")
print (n_negativos,"valor(es) negativo(s)")