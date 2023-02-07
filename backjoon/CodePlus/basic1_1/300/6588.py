import sys
input = sys.stdin.readline

MAX_NUMBER = 1000001
SosuList = [True] * (MAX_NUMBER)
for i in range(3,1001,2):
    if SosuList[i]:
        for k in range(i+i, MAX_NUMBER, i):
            SosuList[k] = False

while True:
    N = int(input())
    if N == 0:
        break

    for A in range(3,N,2):
        if SosuList[A] == True and SosuList[N-A] == True:
            print("{0} = {1} + {2}".format(N,A,N-A))
            break