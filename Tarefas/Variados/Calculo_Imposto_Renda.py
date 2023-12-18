sal_bruto = float(input())
n_depend = int(input())
desc_depen = n_depend*137.99
inss = 0
aliquota = 0
deducao = 0

if sal_bruto<=1372.81:
    aliquota =  0
elif sal_bruto>1372.81 or sal_bruto>=2743.25:
    aliquota = 0.15
    deducao = 205.92
elif sal_bruto>2743.25:
    aliquota = 0.275
    deducao = 548.82

if sal_bruto<=720:
    inss =  sal_bruto*0.0765
elif sal_bruto>720 and sal_bruto<=1200:
    inss = sal_bruto*0.09
elif sal_bruto>1200 and sal_bruto<=2400:
    inss = sal_bruto*0.11
elif sal_bruto>2400:
    inss = 2400*0.11

irrf = (sal_bruto - desc_depen - inss)*aliquota - deducao
print (f"{irrf:.2f}")