qntd_aerop, qntd_voos = [int(w) for w in input().split()]
cont = 0

while qntd_aerop != 0 and qntd_voos != 0:
    cont +=1
    maior_trafego = 0
    trafegos = []
    aeroportos = dict()

    for i in range(1,qntd_aerop+1):
        aeroportos.setdefault(i,0)

    for j in range(qntd_voos):
        embarque, desembarque = [int(w) for w in input().split()]
        aeroportos[embarque] += 1
        aeroportos[desembarque] += 1
    
    maior_trafego = max(aeroportos.values()) # pego o maior valor do dicionário
    
    for chave,valor in aeroportos.items(): # pecorro o dicionario variando as chaves e os valores
        if valor == maior_trafego: # qundo eu encontro valor que quero
            trafegos.append(chave) # salvo a chave desse valor em uma lista
            
    print("Teste", cont)       
    print(' '.join(map(str, trafegos)))
    qntd_aerop, qntd_voos = [int(w) for w in input().split()]