import sys

test = int(input())
for i in range(test):
    a='*'*(i+1)
    b=' '*(test-i-1)
    print('{}{}'.format(b,a))