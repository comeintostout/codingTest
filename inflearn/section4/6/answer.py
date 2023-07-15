import sys
sys.stdin = open("in5.txt","rt")

players = []

N = int(input())
for i in range(N):
    players.append(list(map(int,input().split())))

players.sort(key=lambda x:(x[0],x[1]))
answer = [[0,10000]]

for player in players:
    prev = answer[-1]
    while player[1] >= prev[1] and answer:
        answer.pop()
        prev = answer[-1]
    answer.append(player)
print(len(answer)-1)