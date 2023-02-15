import sys
input = sys.stdin.readline

TC = int(input())
for _ in range(TC):
    N = int(input())
    A = list(map(int,input().rstrip().split()))
    B = list(map(int,input().rstrip().split()))

    DP = [ [0,0,0] for i in range(N+1) ]
    DP[1][1] = A[0]
    DP[1][2] = B[0]

    for i in range(2,N+1):
        DP[i][0] = max(DP[i-1])
        DP[i][1] = max(DP[i-1][0], DP[i-1][2]) + A[i-1]
        DP[i][2] = max(DP[i-1][0], DP[i-1][1]) + B[i-1]

    print(max(DP[N]))