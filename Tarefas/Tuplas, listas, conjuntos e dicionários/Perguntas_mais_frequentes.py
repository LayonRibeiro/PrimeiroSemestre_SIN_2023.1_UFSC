num_perguntas, ind_frequente = [int(w) for w in input().split()]

while num_perguntas!=0 and ind_frequente != 0:
    perguntas = [int(w) for w in input().split()]
    maior_repet = 0
    for x in set(perguntas):
        repet = perguntas.count(x)
        if repet >= ind_frequente:
            maior_repet = x
    print(maior_repet)
        
    num_perguntas, ind_frequente = [int(w) for w in input().split()]
