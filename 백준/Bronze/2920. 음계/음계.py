N=list(map(int,input().split()))
M=[1,2,3,4,5,6,7,8]
M_reverse=sorted(M,reverse=True)
if(N==M):
    print("ascending")
elif (N==M_reverse):
    print("descending")
else:
    print("mixed")