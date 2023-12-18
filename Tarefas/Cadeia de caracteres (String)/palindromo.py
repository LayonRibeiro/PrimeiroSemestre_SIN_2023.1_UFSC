frase = input()
frase_limpa = "" # armazena apenas as letras; os demais caracteres são descartados ("-" ; ":" ; ".")

for letra in frase.lower():     # percorre a frase caracter a caracter, já toda em letras minúsculas
    if letra.isalpha(): # se o caracter for uma letra, concatena na frase limpa
        frase_limpa += letra

print(frase_limpa == frase_limpa[::-1]) # compara a frase com ela invertida para ver se são iguais