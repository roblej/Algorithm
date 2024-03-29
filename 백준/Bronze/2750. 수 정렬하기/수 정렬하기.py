N=int(input())
M=[]
empty=0
for i in range(N):
    M.append(int(input()))
for i in range(N):
    for i in range(N-1):
        if(M[i]>M[i+1]):
            empty=M[i]
            M[i]=M[i+1]
            M[i+1]=empty
for i in range(N):
    print(M[i])