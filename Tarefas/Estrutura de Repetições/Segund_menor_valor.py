tam = int(input())
seq = []

for i in range(tam):
    n = int(input())
    seq.append(n)
    seq.sort()

print(seq[1])