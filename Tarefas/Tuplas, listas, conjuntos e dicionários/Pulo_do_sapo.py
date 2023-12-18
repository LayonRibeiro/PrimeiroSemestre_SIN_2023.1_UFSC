limite, qtdade = [int(x) for x in input().split()]
alturas = [int(x) for x in input().split()]
resultado = "YOU WIN"

for i in range (len(alturas)-1):
    if abs(alturas[i]-alturas[i+1]) > limite or abs(alturas[i+1]-alturas[i]) > limite:
        resultado = "GAME OVER"
        break
print(resultado)     