X=[]
for i in range (9):
    X.append(int(input()))
max = X[0]
line=1
for i in range(9):
    if(max<X[i]):
        max=X[i]
        line=i+1
    
print(max)
print(line)