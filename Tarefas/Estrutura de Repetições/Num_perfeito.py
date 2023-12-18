l = int (input())
for l in range (l):
    num = int(input())
    soma = 0
    div = num//2

    if num%2 == 0:
        for i in range (1,div+1,1):
            if num%i == 0:
                soma += i
                
    if soma == num:
        print(num,"eh perfeito")
    else:
        print(num,"nao eh perfeito")
