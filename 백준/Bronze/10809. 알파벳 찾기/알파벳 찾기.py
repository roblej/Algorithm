N = [-1 for _ in range (26)]
M = [chr(i) for i in range(ord('a'),ord('z')+1)]
input=list(map(str,input()))
for i in range(len(input)): #backjoon 0~7
    K = M.index(input[i]) # K는 a~z리스트에서 b의 인덱스 2번째
    if(N[K]==-1):
        N[K] = i #-1의 리스트에서 b의 인덱스는 
N=" ".join(str(x) for x in N)
print(N)