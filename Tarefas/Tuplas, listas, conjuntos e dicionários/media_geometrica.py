x = int(input())
num = []
mult = 1

for i in range(x):
    num.append(float(input()))
    mult *= num[i]
    
print(mult**(1/len(num)))