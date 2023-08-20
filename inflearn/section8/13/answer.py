import sys
sys.stdin= open('in5.txt','rt')

N = int(input())
friendship = [[0]*(N+1) for _ in range(N+1)]

while True:
    f1,f2 = map(int,input().split())
    if f1 == -1 and f2 == -1:
        break
    friendship[f1][f2] = 1
    friendship[f2][f1] = 1

for k in range(1,N+1):
    for f1 in range(1,N+1):
        for f2 in range(1,N+1):
            if f1 == f2 or k ==f1 or k == f2:
                continue
            if friendship[f1][k] and friendship[k][f2]:
                if friendship[f1][f2]:
                    friendship[f1][f2] = friendship[f2][f1] = min(friendship[f1][f2], friendship[f1][k]+ friendship[k][f2])
                else:
                    friendship[f1][f2] = friendship[f2][f1] = friendship[f1][k]+ friendship[k][f2]
   
score = [0]*(N+1)
for i in range(1,N+1):
    score[i] = max(friendship[i])
minScore = min(score[1:])
winners= []
for i in range(1,N+1):
    if score[i] == minScore:
        winners.append(i)
print(minScore, len(winners))
for w in winners:
    print(w,end=" ")
print()