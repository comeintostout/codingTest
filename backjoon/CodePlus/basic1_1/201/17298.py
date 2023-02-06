import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().strip().split()))
NGE = [ -1 ] * N

undecided =[0]
for i in range(1,N):
    while undecided and A[undecided[-1]] < A[i]:
        NGE[undecided.pop()] = A[i]
    undecided.append(i)

print(" ".join(map(str,NGE)))
