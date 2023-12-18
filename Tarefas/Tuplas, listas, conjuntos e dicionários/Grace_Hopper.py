frase = [str(x) for x in input().split('-')]
vovo = ["c","o","b","o","l"]
cont = 0

for i in range(len(frase)):
    palavra = frase[i]
    if palavra[0] == vovo[i] or palavra[-1] == vovo[i]:
        cont += 1
    else:
        break

if cont == 5:
    print('GRACE HOPPER')
else:
    print('BUG')