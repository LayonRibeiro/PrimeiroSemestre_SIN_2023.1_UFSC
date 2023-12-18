entrada = []
qntd_bilhetes = int(input())
cont = 0

while qntd_bilhetes != 0:
    while len(entrada) != qntd_bilhetes:
        entrada = [int(x) for x in input().split()]

    for i in range(1,len(entrada)+1):
        if i == entrada[i-1]:
            campeao = i
    
    cont += 1
    print("Teste", cont)
    print(campeao)
    
    qntd_bilhetes = int(input())
