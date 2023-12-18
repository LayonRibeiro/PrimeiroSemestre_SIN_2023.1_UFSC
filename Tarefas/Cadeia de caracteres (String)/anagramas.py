palavra1 = input()
palavra2 = input()

if palavra1 != palavra2 and len(palavra1) == len(palavra2): # verifica se as palavras são difrentes e tpossume o mesmo tamanho
    anagrama = True
    for i in palavra1:
        if palavra1.count(i) != palavra2.count(i):# compara quantas vezes uma letra se repete em cada palavra
            anagrama = False
            break
else:
    anagrama = False

print(anagrama)