import math

def eh_primo(n):
    if  n == 1 or (n!=2 and n % 2 == 0):
        eh_primo =  False
    elif n == 2:
        eh_primo = True
    else:
        eh_primo = True
        raiz =int(math.sqrt(n))
        for i in range (3, raiz+1, 2): #divisão só para n° ímpares
                if n % i == 0:
                    eh_primo = False
                    break
    return eh_primo

n1 =  int(input())
n2 =  int(input())
cont = 0

for n in range (n1,n2+1,1):
    if eh_primo(n):
        cont += 1
        
print(cont)