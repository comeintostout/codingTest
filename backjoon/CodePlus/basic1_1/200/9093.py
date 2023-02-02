import sys

N = int(sys.stdin.readline())

for _ in range(N):
    sentences = map(lambda s: s[::-1], sys.stdin.readline().split())
    print(' '.join(sentences))
