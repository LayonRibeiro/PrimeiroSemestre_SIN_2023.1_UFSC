frase = input().lower()
    
contagem = dict()
for letra in frase:
    if letra in contagem:
        contagem[letra] += 1
    else:
        contagem[letra] = 1
        
maior_ocorrencia = -1
letra_mais_ocorre = ''
for letra, ocorr in contagem.items():
    if ocorr > maior_ocorrencia:
        maior_ocorrencia = ocorr
        letra_mais_ocorre = letra
        
print(letra_mais_ocorre)