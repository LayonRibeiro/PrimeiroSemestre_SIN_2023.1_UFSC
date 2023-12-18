t = int(input("N° de pessoas acessaram o 3° link:"))

while t<0 or t>1000:
    t = int(input("Digite um valor válido, entre 0 e 1000: "))

prim_link = 4*t

print(prim_link)
