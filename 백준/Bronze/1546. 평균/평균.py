N=int(input())
M=list(map(int,input().split()))
maxscore=max(M)
total=0
for i in range(N):
    total += M[i]/maxscore*100
avg = total/N
print(avg)