segundos = abs(int(input("Digite o tempo de duração do evento em segundos: ")))

if segundos>60:
    minutos = int(segundos/60)
    segundos = segundos%60

if minutos>60:
    horas = int(minutos/60)
    minutos = minutos%60

print(horas,":", minutos,":",segundos)