jogadores, jogos = [int(x) for x in input().split()]
gols_em_todas = 0

for i in range(jogadores):
    gols_partida = [int(x) for x in input().split()]
    
    if 0 not in gols_partida:
        gols_em_todas +=1

print(gols_em_todas)