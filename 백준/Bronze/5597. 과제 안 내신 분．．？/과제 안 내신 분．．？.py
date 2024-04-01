N=[]
M=[]
for i in range(28):
    N.append(int(input()))
for i in range(30):
    if i+1 not in N:
        M.append(i+1)
for i in range(len(M)):
    print(M[i])