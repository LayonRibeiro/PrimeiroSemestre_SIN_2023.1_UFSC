num_postos, DIM = [int(w) for w in input().split()]
dist_postos = [int(x) for x in input().split()]

saida = 'S'
for i in range(num_postos-1):
    if dist_postos[i+1]- dist_postos[i] > DIM:
        saida = 'N'
        break

print(saida)