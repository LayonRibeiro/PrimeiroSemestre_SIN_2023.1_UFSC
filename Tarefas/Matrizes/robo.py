qnt_l, qnt_c = [int(x) for x in input().split()]
x, y = [int(x) for x in input().split()]
matriz = [[int(w) for w in input().split()] for _ in range(qnt_l)]

mov = True

pos = []
while mov:

    if x-1 <= qnt_c-1  and matriz[x][y+1] == 1:
        par = (x, y+1)
        if par not in pos:
            while x-1 <= qnt_c-1 and  matriz[x][y+1] == 1:
                y += 1
                pos.append(par)

    if y-1 >= 0 and  matriz[x][y-1] == 1:
        par = (x,y-1)
        if par not in pos:
            while y-1 >= 0 and matriz[x][y-1] == 1:
                y -= 1
                pos.append(par)
    
    if x+1 <= qnt_l-1 and matriz[x+1][y] == 1:
        par = (x+1,y)
        if par not in pos:
            while x+1 <= qnt_l-1  and matriz[x+1][y] == 1:
                x += 1
                pos.append(par)
    
    if  x-1 >= 0 and matriz[x-1][y] == 1:
        par = (x-1,y)
        if par not in pos:
            while x-1 >= 0 and matriz[x-1][y] == 1:
                x -= 1
                pos.append(par)
    else:
        mov = False
    
print(x, y)            
    