num_carros, num_voltas = [int(w) for w in input().split()]
temp_do_carro = []
tempo_volta = []
soma_tempo = 0

for j in range(num_carros):
    while len(tempo_volta) != num_voltas:
        tempo_volta = [int(x) for x in input().split()]
        for x in tempo_volta:
            soma_tempo += x
    
    temp_do_carro.append(soma_tempo)
    tempo_volta.clear()
    soma_tempo = 0
            
ordem =   sorted(temp_do_carro)

for i in range(len(temp_do_carro)):
    if temp_do_carro[i] == ordem[0]:
        campeao = i + 1
    if temp_do_carro[i] == ordem[1]:
        seg_lugar = i + 1
    if temp_do_carro[i] == ordem[2]:
        ter_lugar = i + 1
        
print(campeao)
print(seg_lugar)
print(ter_lugar)