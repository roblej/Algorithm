import sys

while True:
    a,b = map(int, sys.stdin.readline().split())
    c = a+b
    if(a==0 & b==0):
        break
    print('{}'.format(c))