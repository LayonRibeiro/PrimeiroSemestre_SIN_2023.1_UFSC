num = float(input())
inteiros = 0
soma = 0
cont = 0

while num != 0:
    if num / int(num) == 1:
        inteiros += 1
    if num > 0:
        soma += num
        cont += 1
    num = float(input())
    
media = soma/cont

print(inteiros)
print(f"{media:.2f}")