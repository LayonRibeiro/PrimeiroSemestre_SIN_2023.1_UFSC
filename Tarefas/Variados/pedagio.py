l, d = [float(w) for w in input("Digite o comprimento da estrada e a distância entre pedágios: ").split()]

k, p = [float(w) for w in input("Digite custo/km e o valor do pedágio: ").split()]

n_pedagios = l//d

ct_pedagios = p*n_pedagios

ct_km = k*l

ct= ct_pedagios+ct_km

print(f"{ct}")