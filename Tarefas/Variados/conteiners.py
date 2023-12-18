a, b, c = [int(w) for w in input("Digite a largura, comprimento e altura dos contêineres, respectivamente:").split()]

x, y, z = [int(w) for w in input("Digite a largura, comprimento e altura do navio respectivamente:").split()]

a = x//a
b = y//b
c = z//c
    
    
qnt_cont = (a*b*c)
 
print(f"{qnt_cont}")