import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().strip().split()))
F = dict()
NGF = [ -1 ] * N

for i in A:
    if i in F:
        F[i] += 1
    else:
        F[i] = 1

undecided =[0]
for i in range(1,N):
    while undecided and F[A[undecided[-1]]] < F[A[i]]:
        NGF[undecided.pop()] = A[i]
    undecided.append(i)

print(" ".join(map(str,NGF)))
