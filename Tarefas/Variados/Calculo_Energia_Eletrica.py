cons = float(input())
custo = 0
x1 = 0
x2 = 0

if cons <= 30:
    custo = cons*0.09556
elif cons>30 and cons<=100:
    custo = 30*0.09556
    x1 = cons - 30
    custo = custo+(x1*0.16698)
elif cons>100 and cons<=200:
    custo = 30*0.09556
    x1 = cons - 100
    custo = custo+(70*0.16698)+ (x1*0.25052)
elif cons>200:
    custo = 30*0.09556
    x1 = cons - 200
    custo = custo+(70*0.16698)+(100*0.25052)+(x1*0.27836)
    
print(f"{custo:.2f}")  