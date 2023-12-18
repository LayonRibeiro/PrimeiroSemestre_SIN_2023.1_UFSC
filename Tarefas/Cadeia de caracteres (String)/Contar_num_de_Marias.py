num =  int(input())
cont = 0

for i in range(num):
    nome = input()
    nome = nome.upper()
    if ("MARIA " in nome) or ("AIRAM" in nome[:-6:-1]):
        cont += 1  

print(cont)