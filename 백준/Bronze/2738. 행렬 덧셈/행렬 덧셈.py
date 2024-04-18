n, m = map(int, input().split())
first_array = [[0]*m for _ in range(n)]
second_array = [[0]*m for _ in range(n)]
total_array = [[0]*m for _ in range(n)]
for i in range(n):
    array=list(map(int,input().split()))
    for j in range(m):
        first_array[i][j]=array[j]

for i in range(n):
    array2=list(map(int,input().split()))
    for j in range(m):
        second_array[i][j]=array2[j]


for i in range(n):
    for j in range(m):
        total_array[i][j]=first_array[i][j]+second_array[i][j]

for i in range(n):
    for j in range(m):
        if(j==(m-1)):
            print(total_array[i][j])
        else:    
            print(total_array[i][j],end=' ')