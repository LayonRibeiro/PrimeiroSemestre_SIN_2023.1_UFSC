num  = 1
seq = ""

while num != 0:
    num  = int(input())
    if num == 0:
        print("Mary won ",num, "times and John won ",num, "times")
        break
    seq = ""
    while (len(seq) < 2*num) :
        seq += input() + " "
    print("Mary won ",seq.count("0"), "times and John won ",seq.count("1"), "times")