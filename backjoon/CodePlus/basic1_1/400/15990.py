import sys
input = sys.stdin.readline

TC = int(input())

DP = []
MAXN = 0
for _ in range(TC):
    N = int(input())   
    if N < 3:
        print(1)
    else:
        if MAXN != 0 and N <= MAXN:
            print((DP[N][1]+DP[N][2]+DP[N][3])%1000000009)
        else:
            startIdx = 0
            if MAXN == 0:
                DP = [[0,0,0,0] for i in range(N+1)]
                DP[1][2] = DP[1][3] = DP[2][3] = DP[2][1] = 0
                DP[1][1] = DP[2][2] = DP[3][3] =  DP[3][2] = 1
                DP[3][1] = 1
                startIdx = 4
            elif N > MAXN:
                for i in range(N-MAXN):
                    DP.append([0,0,0,0])
                startIdx = MAXN+1

            for i in range(startIdx,N+1):
                DP[i][1] = (DP[i-1][2] + DP[i-1][3]) %1000000009
                DP[i][2] = (DP[i-2][1] + DP[i-2][3])%1000000009
                DP[i][3] = (DP[i-3][1] + DP[i-3][2])%1000000009
            
            MAXN = N
            print((DP[N][1]+DP[N][2]+DP[N][3])%1000000009)
