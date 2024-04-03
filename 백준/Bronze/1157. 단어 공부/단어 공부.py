import sys

N=sys.stdin.readline().upper()
M = set(N)
M.discard('\n')
M = list(M)
N =list(N)
I=[0 for _ in range(len(M))]
for i in range(len(M)):
    for j in range(len(N)-1):
        if(N[j] == M[i]):
            I[i]+=1
J=max(I)
I_count=I.count(J)
K=I.index(J)


if I_count>1:
    print('?')
else:
    print(M[K])
