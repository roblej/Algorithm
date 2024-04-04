N=[]
for i in range(10):
    N.append(int(input()))
M=[]
for i in range(10):
    M.append(N[i]%42)
I=set(M)
A=len(I)
print(A)