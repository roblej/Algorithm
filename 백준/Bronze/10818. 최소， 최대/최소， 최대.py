N=int(input())
X=list(map(int,input().split()))
max=X[0]
min=X[0]
for i in range (N):
    if(max<X[i]):
        max=X[i]
    if(min>X[i]):
        min=X[i]
print(min,max)