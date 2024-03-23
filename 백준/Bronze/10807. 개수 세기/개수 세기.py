N = int(input()) 
N_list = input()
v = int(input())

if len(N_list.split()) == N :
    number_list = list(map(int, N_list.split()))

print(number_list.count(v))