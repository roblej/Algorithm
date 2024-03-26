N,M = map(int,input().split())
X=[0 for i in range(N)]
for i in range(M):
    I,J,K = map(int,input().split())
    for j in range(I-1,J):
        X[j]=K
print(' '.join(str(i) for i in X))