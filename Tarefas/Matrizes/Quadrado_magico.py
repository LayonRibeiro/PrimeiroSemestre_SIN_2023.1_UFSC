ordem = int(input())
matriz = [[int(x) for x in input().split()] for _ in range(ordem)]
constante = 0
magico = True

for i in range(ordem):
    if i == 0:
        constante = sum(matriz[i][0:ordem])
    else:
        if constante != sum(matriz[i][0:ordem]):
            magico = False
            break
if magico:        
    for coluna in range(ordem):
        soma = 0
        for linha in range(ordem):
            soma += matriz[linha][coluna]
        if soma != constante:
            magico = False
            break
    
if magico:     
    soma = 0  
    for w in range(ordem):
        soma += matriz[w][w] + matriz[w][ordem-(1+w)]
    if soma != 2*constante:
        magico = False
    
print(magico)