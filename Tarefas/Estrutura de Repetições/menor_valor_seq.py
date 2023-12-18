tam = int(input())
menor = 0
for i in range(tam):
    n = int(input())
    if i == 0:
        menor = n
    if n < menor:
        menor=n
        
print(menor)