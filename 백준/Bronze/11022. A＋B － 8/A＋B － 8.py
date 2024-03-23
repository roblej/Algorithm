import sys

test = int(input())
for i in range(test):
    a,b = map(int, sys.stdin.readline().split())
    c = a+b
    print('Case #{}: {} + {} = {}'.format(i+1,a,b,c))