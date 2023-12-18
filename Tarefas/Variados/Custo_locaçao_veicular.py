dias = int(input())
km = float (input())

km_cortesia = dias * 60
km = km-km_cortesia
custo = (dias*45)+(km*0.5)

print(custo)    