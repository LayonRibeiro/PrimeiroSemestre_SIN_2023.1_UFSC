num_pessoas = int(input())

while num_pessoas !=0:
    tempo_chegada = [int(w) for w in input().split()]
    tempo_total = 0
    if len(tempo_chegada) == 1:
        tempo_total += 10
    else:
        for i in range(0,len(tempo_chegada)-1):
            sub = tempo_chegada[i+1] - tempo_chegada[i]
            if  sub < 10:
                tempo_total += sub
            else:
                tempo_total += 10
        tempo_total += 10
        
    print(tempo_total) 
    num_pessoas = int(input())
