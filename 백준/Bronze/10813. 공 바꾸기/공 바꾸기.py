N,M = map(int,input().split())
X=[i+1 for i in range(N)]
K=0
for i in range(M):
    I,J = map(int,input().split())
    K=X[I-1]
    X[I-1]=X[J-1]
    X[J-1]=K
print(' '.join(str(i) for i in X))