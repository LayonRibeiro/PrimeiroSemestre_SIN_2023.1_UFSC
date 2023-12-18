num_camisetas  =  int(input())
adivinhas  = []

for _ in range(num_camisetas):

    num_integrantes, num = [int(w) for w in input().split()]
    
    while len(adivinhas) != num_integrantes:
        adivinhas = [int(x) for x in input().split()]
    
    for i in range(len(adivinhas)):
        dist = abs(num-adivinhas[i])
        if i == 0:
            dist_camp = dist
            campeao = i+1
        elif dist < dist_camp:
            dist_camp = dist
            campeao = i+1
    
    print(campeao)