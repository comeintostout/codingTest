import sys
sys.stdin = open("in4.txt","rt")

N,M = map(int,input().split())
dist = [ ["M"]*(N+1) for _ in range(N+1) ]

for i in range(M):
    st,ed,co = map(int,input().split())
    dist[st][ed] = co

for k in range(1,N+1):
    for st in range(1,N+1):
        for ed in range(1,N+1):
            if st == ed:
                dist[st][ed] = 0
                continue
            if dist[st][k] != 'M' and dist[k][ed] != 'M':
                if dist[st][ed] == 'M':
                    dist[st][ed] =  dist[st][k] +dist[k][ed]
                else:
                    dist[st][ed] = min(dist[st][ed], dist[st][k] +dist[k][ed])

for i in range(1,N+1):
    for j in range(1,N+1):
        print(dist[i][j],end=" ")
    print()