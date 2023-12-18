xic,ovos,colher = [int(w) for w in input("Digite a quantidade que voce possui de xicaras defarinha de trigo, ovos e colheres de sopa de leite respectivamente:").split()]

xic = xic//2
ovos = ovos//3
colher = colher//5

bolos = min(xic,ovos,colher)

print(f"Você conseguirá preparar {bolos} bolos")