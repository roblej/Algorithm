N=list(map(int,input().split()))
M=0
for i in range(len(N)):
    M+=N[i]**2
I=M%10
print(I)