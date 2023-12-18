testes = int(input())
print(" ")

while testes != 0:

    total_arv = 0
    arvores = dict()
    qntd = 0
    
    while True:
        especie = input()
        if especie == ' ':
            break
        total_arv += 1
        if especie not in arvores.keys():
            arvores.setdefault(especie,1)
        else:
            arvores[especie] += 1
    
    ordena = sorted(arvores.keys())
    
    for especie, qntd in arvores.items(): #inserir o percentual no dicionario
        arvores[especie] = "{:.4f}".format(qntd/total_arv*100)
    
    for tipo in ordena:
        print(tipo, arvores[tipo])
    
    testes -=1
    print(" ")