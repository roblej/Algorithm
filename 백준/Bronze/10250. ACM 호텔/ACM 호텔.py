import math

N=int(input())
for i in range(N):
    h, w, n =map(int,input().split())
    floor = n % h
    num = n//h +1
    if(floor == 0):
        floor = h
        num -= 1
    
    print(floor * 100 + num)