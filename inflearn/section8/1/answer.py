import sys
from itertools import combinations_with_replacement
sys.stdin = open("in5.txt","rt")

if __name__ == "__main__":
    N = int(input())
    
    DP = [0]*(N+1)
    DP[1] = 1
    DP[2] = 2
    for i in range(3,N+1):
        DP[i] = DP[i-1] + DP[i-2]
    print(DP[N]) 