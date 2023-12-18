num = input()
ind = num.index(".")

tam_parte_int = len(num[:ind])
parte_int = num[:ind]
    
tam_parte_dec = len(num[ind+1:ind+5])
part_dec = num[ind+1:ind+5]
 
if num[0].isalnum() == "-": # n° maior que zero
