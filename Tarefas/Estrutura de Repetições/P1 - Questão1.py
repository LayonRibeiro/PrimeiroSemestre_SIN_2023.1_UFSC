x0, y0 = [int(w) for w in input().split()]
mov = False
x1 = 1

while x1 != 0:
    x1, y1 = [int(w) for w in input().split()]
    mov = x0 == x1 or y0 == y1 or abs(x0-x1) == abs(y0-y1)

    print(mov) 