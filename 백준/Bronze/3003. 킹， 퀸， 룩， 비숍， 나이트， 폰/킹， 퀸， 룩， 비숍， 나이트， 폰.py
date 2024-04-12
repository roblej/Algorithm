N=list(map(int,input().split()))
M=[1,1,2,2,2,8]
I=[]
for i in range(len(N)):
    I.append(M[i]-N[i])
    print(I[i],end=' ')