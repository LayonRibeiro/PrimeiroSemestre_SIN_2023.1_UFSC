ordem = int(input())
while True:
        matriz = [[0] * ordem for _ in range(ordem)]
                
        for i in range(ordem):
            for j in range(ordem):
                matriz[i][j] = (2**i)*(2**j)
        
        n = len(str(matriz[-1][-1]))

        for linha in matriz:
            for x in linha:
                print(f"{x:{n}}", end=' ')
        
            print()
        ordem = int(input())
        if ordem == 0:
            break
        print(' ')
