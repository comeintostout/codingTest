import sys
from collections import deque
sys.stdin = open("in5.txt","rt")

if __name__ == "__main__":
    S,E = map(int,input().split())

    if S > E:
        print(S-E)
    else:
        MAX = 10000
        queue = deque()
        visited = [0] * (MAX+1)
        dis = [0] * (MAX+1)
        queue = deque()
        queue.append(S)

        while queue:
            now = queue.popleft()
            if now == E:
                break
            for nextS in (now-1,now+1,now+5):
                if 0<nextS<=MAX:
                    if visited[nextS] == 0:
                        queue.append(nextS)
                        visited[nextS] = 1
                        dis[nextS] = dis[now]+1

        print(dis[E])