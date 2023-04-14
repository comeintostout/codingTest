import sys
import heapq as hq

FILE_NAME = "2.txt"

sys.stdin = open("in"+FILE_NAME,"rt")

heap = []
while True:
    n = int(input())
    if n == -1:
        break
    
    if n == 0:
        if len(heap) == 0:
            print(-1)
        else:
            print(hq.heappop(heap) * -1)
    else:
        hq.heappush(heap,-1 * n)
