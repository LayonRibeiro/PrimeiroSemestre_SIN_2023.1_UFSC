import math

def montante (cap,tempo,taxa):
    i = taxa/100
    m=cap*((1+i)**tempo)
    return(round(m,2)) #arredondamento com 2 casas decimais
    

cap = float(input("Digite o valor do Capital(R$): "))
tempo = int(input("Quantidade de meses que o capital ficará aplicado: "))
taxa = float(input("Valor da taxa de juros (%): "))

print("O valor do montante será de: ", montante(cap,tempo,taxa))


