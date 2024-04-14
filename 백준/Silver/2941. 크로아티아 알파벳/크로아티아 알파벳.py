N=['c=','c-','dz=','d-','lj','nj','s=','z=']
M=input()

for i in N:
    M=M.replace(i,'*')
print(len(M))