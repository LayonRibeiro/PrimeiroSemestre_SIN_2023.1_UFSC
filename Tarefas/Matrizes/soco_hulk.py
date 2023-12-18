num = int(input())

for _ in range(1,num+1):
    qntd_l, qntd_c , x0 , y0 = [int(x) for x in input().split()]
    x0 -= 1
    y0 -= 1
    
    matriz = [[int(w) for w in input().split()] for _ in range(qntd_l)]

    for i in range(qntd_l):
        for j in range(qntd_c):
            if i != x0 or j != y0:
                a = abs(x0 - i)
                b = abs(y0 - j)
                if max(a,b) <= 9:
                    matriz[i][j] += 10 - max(a, b)
                else:
                    matriz[i][j] += 1
            else:
                matriz[i][j] += 10
    
    print(f"Parede {_}:")
    for linha in matriz:
        print(*linha, end = ' ')
        print(" ")
    
    