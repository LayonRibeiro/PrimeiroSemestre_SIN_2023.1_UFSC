num = int(input())

for _ in range(num):
    grandeza, tamanho = [int(x) for x in input().split()]
    matriz = [[int(x) for x in input().split()] for _ in range(tamanho)]
    qntd_dd_validos = 3 
    dicionario = dict()
    
    for i in range(tamanho):
        xy = matriz[i][1:3]
        x , y = xy
        xy = str(x)+" "+str(y)
       
        for  w in range(i+1, tamanho):
            pq = matriz[w][1:3]
            p , q = pq
            pq = str(p)+" "+str(q)
            
            if xy == pq and xy in dicionario:
                dicionario[xy] += matriz[w][qntd_dd_validos]
            elif xy == pq and xy not in dicionario:
                soma = matriz[i][qntd_dd_validos]+matriz[w][qntd_dd_validos]
                dicionario.setdefault(xy, soma)
            if xy not in dicionario:
                dicionario.setdefault(xy, matriz[i][qntd_dd_validos])
            if pq not in dicionario:
                dicionario.setdefault(pq, matriz[w][qntd_dd_validos])

    for chave, valor in sorted(dicionario.items()):
        print(chave, valor)
    
    print('')
