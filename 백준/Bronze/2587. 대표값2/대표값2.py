N=[]
for i in range(5):
    N.append(int(input()))
total = 0
median = 0
for i in range(len(N)):
    total+=N[i]
avarage = int(total/len(N))
print(avarage)
N.sort()
median=N[2]
print(median)