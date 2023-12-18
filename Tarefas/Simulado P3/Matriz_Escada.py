num_lin, num_col = [int(x) for x in input().split()]
matriz = [[int(x) for x in input().split()] for _ in range(num_lin)]

escada = True

for l in range(num_lin):
    if escada == False:
        break
        
    for c in range(num_col):
        # analisa a esquerda do elemento
        if matriz[l][c] != 0:
            intervalo = matriz[l][0:c]
            if intervalo.count(0) == len(intervalo):
                # analisa a coluna  
                for j in range(c, num_col):
                    for i in range(l+1, num_lin):
                        if matriz[i][j] != 0:
                            escada = False
                            break
                    break
            else:
                escada = False
            
            if escada: #pula para a próxima linha
                break
            
        # se posição for igual a zero
        else:# todas as posições abaixo terá de ser igual a zero
            for j in range(c, num_col):
                for i in range(l+1, num_lin):
                    if matriz[i][j] != 0:
                        escada = False
                        break
                break
            
if escada:
    print("S")
else:
    print("N")