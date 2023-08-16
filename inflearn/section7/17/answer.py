from itertools import combinations
import sys
sys.stdin = open("in5.txt","rt")

if __name__=="__main__":
    N, M = map(int,input().split())
    Town = [list(map(int,input().split())) for _ in range(N)]
    Houses= []
    Pizza = []

    for r in range(N):
        for c in range(N):
            if Town[r][c]==1:
                Houses.append((r,c))
            if Town[r][c]==2:
                Pizza.append((r,c))

    minDist = 999999999
    for comb in combinations(Pizza,M):
        dist=0
        for h in Houses:
            dist += min(list(map(lambda p: abs(p[0]-h[0])+abs(p[1]-h[1]) ,comb)))
        minDist= min(minDist, dist)

    print(minDist)