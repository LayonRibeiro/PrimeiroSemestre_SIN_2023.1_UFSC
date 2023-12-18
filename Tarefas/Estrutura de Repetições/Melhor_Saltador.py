num_salt = int(input())
maior_salto = 0
campeao = ""

for i in range (1,num_salt+1,1):
    nome = str(input())
    
    if i == 1:
        campeao = nome
    
    for j in range(3):
        salto = float(input())
        
        if i==1 and j==0:
            maior_salto = salto
        
        if salto > maior_salto:
            maior_salto = salto
            campeao = nome
            print("O melhor é:",maior_salto, "de", campeao)
           
            
print(campeao)