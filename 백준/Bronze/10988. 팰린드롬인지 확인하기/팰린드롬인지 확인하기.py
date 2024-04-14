N=list(input())
M=N[::-1]
count=0
for i in range(len(N)):
    if(M[i]==N[i]):
        count+=1

if(count==len(N)):
    print(1)
else:
    print(0)
