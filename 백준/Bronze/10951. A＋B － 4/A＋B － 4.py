import sys

while True:
    try:
        a,b = map(int, sys.stdin.readline().split())
        c = a+b
        print('{}'.format(c))
    except:
        break