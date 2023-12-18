n1 = int(input())
n2 = int(input())
mult = []

for i in range(1,n2+1,1):
    if n1*i<=n2: 
        mult.append(n1*i)
print(mult)      