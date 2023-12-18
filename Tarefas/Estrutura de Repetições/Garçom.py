n = int(input())
copos_queb = 0

for i in range (n):
    l, c = [int(w) for w in input().split()]
    if l>c:
        copos_queb += c
        
print(copos_queb)
