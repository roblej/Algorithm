A=int(input())
B=int(input())
C=int(input())
D=A*B*C
D = [int(digit) for digit in str(D)]
E=[0 for i in range(10)]
for i in range(10):
    for j in range(len(D)):
        if(D[j]==i):
            E[i]+=1
    print(E[i])
