import math

area = int(input("Valor da área a ser pintada:"))
litros_galao=3.6
area_por_galao= litros_galao*18
valor_galao=25

while area<0:
    area = int(input("VALOR INVÁLIDO.Valor da área a ser pintada:"))

if int(area%area_por_galao) == 0:
    num_de_galoes = int(area/area_por_galao)
else:
    num_de_galoes = int(area/area_por_galao)
    num_de_galoes = num_de_galoes+1

orçamento = num_de_galoes*valor_galao

print("Área de cobertura:", area)
print("Número de galões de tintas necessários: ", num_de_galoes)
print("Valor do orçamento: R$",orçamento)