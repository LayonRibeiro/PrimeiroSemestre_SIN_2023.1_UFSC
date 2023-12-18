import math

def eh_primo(j):
    if  j == 1 or (j!=2 and j % 2 == 0):
        eh_primo =  False
    elif j == 2:
        eh_primo = True
    else:
        eh_primo = True
        raiz =int(math.sqrt(j))
        for i in range (3, raiz+1, 2): #divisão só para n° ímpares
                if j % i == 0:
                    eh_primo = False
                    break
    return eh_primo


n = int(input())
m = int(input())
p1 = n
p2 = m

for i in range (n,2,-1):
    if eh_primo(i) == True:
        p1 = i
        break
    
while eh_primo(p2) == False:
    p2 += 1

print(p1*p2)
    