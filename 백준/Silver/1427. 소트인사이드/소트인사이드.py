N=input()
N_list=[int(digit) for digit in str(N)]
N_len=len(N_list)
M=0
for i in range(N_len):
    for i in range(N_len-1):
        if(N_list[i]<N_list[i+1]):
            M=N_list[i]
            N_list[i]=N_list[i+1]
            N_list[i+1]=M
for i in range(N_len):
    print(N_list[i],end='')