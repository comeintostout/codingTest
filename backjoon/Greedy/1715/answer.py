import heapq

input = open(0).readline

Decks = []
N = int(input())
for i in range(N):
    heapq.heappush(Decks, int(input()))

cnt = 0
while len(Decks) > 1:
    a = heapq.heappop(Decks)
    b = heapq.heappop(Decks)
    cnt += (a+b)
    heapq.heappush(Decks,a+b)
print(cnt)