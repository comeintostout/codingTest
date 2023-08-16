import sys
sys.stdin = open("in5.txt","rt")

def DFS(l):
    global DP
    if DP[l]:
        return DP[l]
    else:
        DP[l] = DFS(l-1) + DFS(l-2)
        return DP[l]

if __name__ == "__main__":
    N = int(input())
    DP = [0]*(N+1)
    DP[1] = 1
    DP[2] = 2
    
    print(DFS(N))
