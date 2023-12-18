num_listas = int(input())
lista_organizada = []

for i in range(num_listas):
    lista = [str(x) for x in input().split()]
    lista2 = list(set(lista))
    
    for j in range(len(lista)):
        if len(lista2) == 0:
            break
        elif lista[j] in lista2:
            lista_organizada.append(lista[j])
            lista2.remove(lista[j])
        
    print(' '.join(map(str, lista_organizada)))
    lista = []
    lista_organizada = []