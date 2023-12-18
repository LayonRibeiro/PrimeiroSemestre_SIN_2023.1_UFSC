num = int(input())
z = num
x = True

while num%2 ==0:
    num /= 2

while num%3 ==0:
    num /= 3
    
while num%5 ==0:
    num /= 5

if num != 1:
    x = False
if z == 1:
    x = False

print(x)