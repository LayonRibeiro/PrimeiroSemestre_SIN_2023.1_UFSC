import math

sal_bruto = 2500.00
horas = 200
valor_hora = (sal_bruto/200)

horas_trabalhadas = int(input("Carga horária (0-200)h  feita pelo funcionário no mês: "))   
while horas_trabalhadas<0 or horas_trabalhadas > horas :
    horas_trabalhadas = int(input("VALOR INVÁLIDO. Digite um N° entre 0 e 200 para as horas trabalhadas:"))

horas_faltadas = horas - horas_trabalhadas
print("As faltas na caraga horária do funcionário corresponde a: ",horas_faltadas,"horas")

horas_extras= int(input("Digite o N° de horas extras feitas pelo funcionário no mês:"))
while horas_extras<0 or horas_extras>horas:
    horas_extras = int(input("VALOR INVÁLIDO. Digite um N° entre 0 e 200 para as horas extras:"))

faltas = float(valor_hora*horas_faltadas)

extras = float(valor_hora*1.2*horas_extras)

sal_bruto= float(sal_bruto + extras - faltas)

#INSS
inss= sal_bruto*0.09

#IR
imposto_de_renda = (sal_bruto*0.13)

sal_liq= sal_bruto-(inss+imposto_de_renda)

print(f"O sálario bruto do funcionário foi de:R${sal_bruto:.2f}")
print(f"Desconto do Imposto de Renda:R${imposto_de_renda:.2f}")
print(f"Desconto do INSS:R${inss:.2f}")
print(f"O sálario líquido do funcionário foi de:R${sal_liq:.2f}")


    
