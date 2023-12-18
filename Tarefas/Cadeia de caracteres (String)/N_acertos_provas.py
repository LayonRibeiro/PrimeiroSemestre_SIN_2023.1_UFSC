gaba = input()
resposta = input()
resultado = 0

for alternativa in range(len(gaba)):
    if gaba[alternativa] == resposta[alternativa]:
        resultado += 1

print(resultado)