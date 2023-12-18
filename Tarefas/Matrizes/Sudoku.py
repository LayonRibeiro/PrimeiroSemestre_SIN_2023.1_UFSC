instancia = int(input())

for p in range(1,instancia+1):
    matriz = [[int(x) for x in input().split()] for _ in range(9)]
    solu = True
    
    #pecorre linha por linha
    for lin in range(9):
        conj = set()
        conj = matriz[lin]
        if len(conj) != 9:
            solu = False
            break
        
    #pecorre coluna por coluna
    if solu:
        for col in range(9):
            conj = set()
            for lin in range(9):
                conj.add(matriz[lin][col])
            if len(conj) != 9:
                solu = False
                break
    
    #pecorre os quadrados
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            conj = set()
            for x in range(i, i + 3):
                for y in range(j, j + 3):
                    conj.add(matriz[x][y])
            if len(conj) != 9:
                solu = False
                break
    if solu:
        print("Instancia",p)
        print("SIM")
    else:
        print("Instancia",p)
        print("NAO")     