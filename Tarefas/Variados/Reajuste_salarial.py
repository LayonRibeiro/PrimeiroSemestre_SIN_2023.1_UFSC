sal = float(input())
sal_min = 1380.60

if sal<(3*sal_min):
    aum = sal*0.20
    sal = sal + aum
elif sal>=(3*sal_min) and sal<=(5*sal_min):
    aum = sal*0.15
    sal = sal+aum
elif sal>(5*sal_min):
    aum = sal*0.10
    sal = sal + aum

if sal<(1.5*sal_min):
    aum = sal
    sal=1.5*sal_min
    aum = sal - aum
    print(f"{aum:.2f}")
    print (f"{sal:.2f}")
elif sal>(20*sal_min):
    sal=20*sal_min
else:
    print(f"{aum:.2f}")
    print (f"{sal:.2f}")
