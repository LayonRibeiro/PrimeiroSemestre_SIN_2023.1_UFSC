venda = float(input())
desc1=0
x = 0

if venda>=500:
    desc = venda*0.3
    
if venda>=1000:
    desc = desc + venda*0.15
    
if venda<500:
    desc = desc+venda*0.2
    
print(f"{venda-desc:.2f}")