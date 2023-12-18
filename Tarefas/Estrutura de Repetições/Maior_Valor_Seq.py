n =  int(input())
maior = 0
pos = 0

for i in range(1,n+1,1):
    n1 =  int(input())
    if i == 0:
        maior = n1
        pos = i
    
    if n1 > maior:
        maior = n1
        pos =i
        
print(maior, pos)