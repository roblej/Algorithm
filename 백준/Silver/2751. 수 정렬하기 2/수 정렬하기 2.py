import sys

N = int(sys.stdin.readline())
M = [int(sys.stdin.readline()) for _ in range(N)]
M.sort()

sys.stdout.write('\n'.join(map(str, M)) + '\n')
