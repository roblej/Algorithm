total_array = [[0]*9 for _ in range(9)]
max = total_array[0][0]
n= 0
m = 0
for i in range(9):
    temp_array=list(map(int,input().split()))
    
    for j in range(9):
        total_array[i][j]=temp_array[j]
        if(max<=temp_array[j]):
            max=temp_array[j]
            n = i+1
            m = j+1
print(max)
print(n, m)