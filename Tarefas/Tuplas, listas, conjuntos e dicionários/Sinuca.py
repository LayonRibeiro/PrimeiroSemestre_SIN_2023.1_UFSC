num_bolas = int(input())
seq_bolas = [int(x) for x in input().split()]

while len(seq_bolas) !=1:
    x = []
    for i in range(len(seq_bolas)-1):
        if seq_bolas[i] != seq_bolas[i+1]:
            x.append(-1)
        else:
            x.append(1)
    seq_bolas = x

if seq_bolas[0] == 1:
    print("preta")
else:
    print("branca")