vendas =  int(input())
total = 0
alcool = 0
gasolina = 0
diesel = 0

for i in range (vendas):
    comb, litros = [float(w) for w in input().split(":")]
    
    if comb == 1:
        total += litros*4.5
        alcool += litros
    elif comb == 2:
        total += litros*5.13
        gasolina += litros
    elif comb == 3:
        total += litros*4.89
        diesel += litros

print(f"Álccol: {alcool:.0f} litros")
print(f"Gasolina: {gasolina:.0f} litros")
print(f"Diesel: {diesel:.0f} litros")
print(f"Total das vendas: R${total:.2f}")  