nome_comp = [str(x) for x in input().split()]
nome_abrev = ""

for nome in range(len(nome_comp)):
    if nome!=0 and len(nome_comp[nome]) > 3:
        parte = nome_comp[nome]
        x = parte[0]
        if nome + 1 == len(nome_comp):
            nome_abrev += nome_comp[nome]
            break
        else:
            nome_abrev += x+". " 
    else:
        nome_abrev += nome_comp[nome]+" "
print(nome_abrev)