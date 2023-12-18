esc_origem = input()
t1 = float(input())
esc_destino = input()
t2 = 0

if esc_origem == "c" and esc_destino == "k":
    t2 = t1+273.15
elif esc_origem == "c" and esc_destino == "f":
    t2 = t1*1.8+32
elif esc_origem == "k" and esc_destino == "c":
    t2 = t1-273.15
elif esc_origem == "k" and esc_destino == "f":
    t2 = (t1-273.15)*1.8+32
elif esc_origem == "f" and esc_destino == "c":
    t2 = (t1-32)/1.8
elif esc_origem == "k" and esc_destino == "k":
     t2 = ((t1-32)/1.8)+273.15

print (t2)