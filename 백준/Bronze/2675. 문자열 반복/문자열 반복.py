import sys

N = int(sys.stdin.readline().strip())
for j in range(N):
    parts = sys.stdin.readline().strip().split()
    I = int(parts[0])
    J = parts[1]
    K = J * I
    for i in range(len(J)):
        A=J[i]*I
        sys.stdout.write(A)
        if(i==len(J)-1):
            sys.stdout.write("\n")
