num_praia = int(input())
praia = []
dist = []
maior_dist = 0
media = 0
soma = 0
cont = 0

for i in range(num_praia):
    local = input()
    distancia = int(input())
    praia.append(local)
    dist.append(distancia)

for l in range(len(dist)):
    soma += dist[l]
    if dist[l]>=15 and dist[l]<=20:
        cont += 1     
    for j in range(l+1, len(dist)):
        if  dist[l] < dist[j] and maior_dist < dist[j]:
            maior_dist = dist[j]
            indice = j
            
media = (soma/len(dist))
print(f"{praia[indice]}, {cont}, {media:.1f}") 