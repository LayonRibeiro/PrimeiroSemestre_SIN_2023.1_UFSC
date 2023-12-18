cpf = input()
so_num = ""
cont = 10
soma = 0
validacao = False

for digito in cpf:
    if digito.isdigit(): # se o caracter for um n° ele adiciona
        so_num += digito
        
if so_num == so_num[::-1]:
    validacao = False
elif len(so_num) == 11:
    for i in so_num[:-2]:
        i = int(i)
        soma += i*cont
        cont -= 1
    if 11-(soma%11) == int(so_num[-2]) or (soma%11 == 0 and int(so_num[-2]) == 0): #Verificação do primeiro Dígito Verificador
        soma = 0
        cont = 10
        for i in so_num[1:-1]: #Cálculo para o segundo Dígito Verificador
            i = int(i)
            soma += i*cont
            cont -= 1
        if 11-(soma%11) == int(so_num[-1]) or (soma%11 == 0 and int(so_num[-1]) == 0): #Verificação do segundo Dígito Verificador
            validacao = True
else:
    validacacao = False
       
print(validacao)