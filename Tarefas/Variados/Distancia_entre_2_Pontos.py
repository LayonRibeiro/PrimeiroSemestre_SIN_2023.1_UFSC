import math

x1, y1 = [float(w) for w in input("Digite as coordernadas do 1° ponto no modelo x,y: ").split]
# a virgula no split(",") é o parametro para que o código reconhça onde vai ser feita a divisão
print(x1)
print(y1)

pp, py = [float(z) for z in input("Digite as coordernadas do 1° ponto no modelo x,y: ").split()]
print(pp)
print(py)

distancia = math.sqrt(((pp-x1)**2)+((py-y1)**2))

print(f"A distância entre os dois pontos é de: {distancia:.4f}")