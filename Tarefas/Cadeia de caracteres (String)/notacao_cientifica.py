import math
num = float(input())

sinal = '+'

if num < 0:
    sinal = '-'
    num *= -1

expo = math.floor(math.log(num, 10))
num_final = num / (10 ** expo)

print(f'{sinal}{num_final:.4f}E{expo:+03d}')