while True:
    try:
        linha, coluna = [int(w) for w in input().split()]
        matriz = []
        
        for i in range(linha):
            linhas = [int(w) for w in input().split()]
            for j in range(len(linhas)):
                if linhas[j] == 1:
                    x1 = i
                    y1 = j
                elif linhas[j] == 2:
                    x2 = i
                    y2 = j
            matriz.append(linhas)

        tempo = abs(x1-x2) + abs(y1-y2)
        print(tempo)
    except EOFError:
        break