valor =  float(input())
classe = input()
proc_carro = input()
idade = int(input())
premio = 0
desc = 0

if proc_carro == "nacional":
    premio = valor*0.1
elif proc_carro == "importado" :
    premio = valor*0.15

if classe == "a":
    desc = premio*0.3
elif classe == "b":
    desc = premio*0.2
elif classe == "c":
    desc = premio*0.1
elif classe == "d":
    desc = premio*0.05

if idade>24:
    desc = desc+(premio*0.1)

print(premio-desc)