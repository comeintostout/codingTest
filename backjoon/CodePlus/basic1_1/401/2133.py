N = int(input())

if N == 1:
    print(0)
else:
    DP = [ [0,0,0,0,0,0,0,0] for _ in range(N+1)]
    DP[1] = [0,1,0,1,0,0,0,1]
    for i in range(2,N+1):  
        DP[i][0] = DP[i-1][1] + DP[i-1][3] + DP[i-1][7]
        DP[i][1] = DP[i-1][0] + DP[i-1][6]
        DP[i][2] = DP[i-1][5]
        DP[i][3] = DP[i-1][0] + DP[i-1][4]
        DP[i][4] = DP[i-1][3]
        DP[i][5] = DP[i-1][2]
        DP[i][6] = DP[i-1][1]
        DP[i][7] = DP[i-1][0]
    print(DP[N][0])