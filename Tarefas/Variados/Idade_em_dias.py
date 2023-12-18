n_dias = int(input("Digite sua idade em n° de dias: "))

anos = n_dias//365
dias = n_dias%365
mes = dias//30
dias = dias%30

print(f" ano(s):{anos}, mes(es):{mes},dia(s):{dias}")