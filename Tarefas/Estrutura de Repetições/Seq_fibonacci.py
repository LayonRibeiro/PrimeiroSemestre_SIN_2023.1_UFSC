#Recursiva de Fibonacci
def fibonacci_rec(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_rec(n - 1) + fibonacci_rec(n - 2)

termo = int(input())
while termo < 0 :
    termo = int(input())

print(fibonacci_rec(termo))

#Sequencial de Fibonacci
def fibonacci_seq(n):
    seq_fibonaci = [0,1]
    if n==0:
        return(seq_fibonaci[0])
    elif n==1:
        return(seq_fibonaci[1])
    else:
        while n+1 != len(seq_fibonaci):
            seq_fibonaci.append(seq_fibonaci[-1]+ seq_fibonaci[-2])
        return(seq_fibonaci[-1])

termo = int(input())
while termo < 0 :
    termo = int(input())
print(fibonacci_seq(termo))