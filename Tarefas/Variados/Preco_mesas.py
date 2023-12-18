comp = float(input())
larg = float(input())
n_gavetas = int(input())
tipo_madeira = input()
preco=0

preco = preco + (n_gavetas*30)
preco = preco + ((comp*larg)*100)

if (comp*larg)>2:
    preco = preco + 50

if tipo_madeira == "mogno":
    preco = preco + 150
elif tipo_madeira == "carvalho":
    preco = preco + 125

if preco<200:
    preco = 200

print(preco)