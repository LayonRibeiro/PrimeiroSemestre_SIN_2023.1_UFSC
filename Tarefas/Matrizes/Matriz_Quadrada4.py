ordem = int(input())

while ordem > 3:
    matriz = [[0] * ordem  for _ in range(ordem)]

    resto = ordem%3
    quoc = ordem//3

    for i in range(ordem):
        for j in range(ordem):
            if i == j:
                matriz[i][j] = 2
            elif i+j == ordem-1:
                matriz[i][j] = 3
            if i==j and i+j == ordem-1:
                matriz[i][j] = 4
                
    for i in range(quoc, 2*quoc+resto):
        for j in range(quoc, 2*quoc+resto):
            if matriz[i][j] != 4:
                matriz[i][j] = 1

    for linha in matriz:
        print(''.join(str(elem) for elem in linha))
        
    ordem = int(input())