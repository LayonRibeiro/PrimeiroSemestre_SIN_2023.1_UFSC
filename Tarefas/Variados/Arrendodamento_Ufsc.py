n1,n2 = [float(w) for w in input().split(".")]

n2 = n2/100

if n2<0.25:
    n2 = 0
elif n2>=0.25 and n2<0.75:
    n2 = 0.5
elif n2>= 0.75:
    n2 = 1

nf = n1+n2
print(f"{nf:.2f}")