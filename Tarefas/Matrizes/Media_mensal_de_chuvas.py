matriz = [[int(x) for x in input().split()] for _ in range(12)]
medias = []

for linha in matriz:
    medias.append(round((sum(linha)/len(linha)),2))

for mes in medias:
    print(mes, end=' ')