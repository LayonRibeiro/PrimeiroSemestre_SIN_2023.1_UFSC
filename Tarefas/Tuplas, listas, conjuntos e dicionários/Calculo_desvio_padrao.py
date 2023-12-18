import math
qntd = int(input())
num = []
somatorio = 0

for i in range(qntd):
    num.append(float(input()))

media = sum(num)/(len(num))

for i in range(qntd):
    somatorio += (num[i]-media)**2
    
print(math.sqrt((somatorio)/(len(num)-1)))