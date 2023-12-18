letras =  input()
codigo = input()
dicionario = dict()
dicionario[' '] = ' '
dicionario['!'] = '!'

for caracter,letra in zip(codigo,letras):
    dicionario.setdefault(caracter, letra) # essa função colocar uma nova chave (caso ela não existir), e atribui um valor a ela

frase = input()
mensagem = ''

for elemento in frase:
        mensagem += dicionario[elemento]

print(mensagem)