ata, beck = [float(x) for x in input().split()]

while ata != 0 and beck != 0:
    dist_ata = [float(x) for x in input().split()]
    menor_dist_ata = min(dist_ata)
    
    dist_beck = [float(x) for x in input().split()]
    dist_beck = sorted(dist_beck)
    
    if menor_dist_ata < dist_beck[1]:
        print("Y")
    else:
        print("N")
        
    ata, beck = [float(x) for x in input().split()]