import sys
sys.stdin = open("in4.txt","rt")

confs = []

N = int(input())
for i in range(N):
    confs.append(list(map(int,input().split())))

confs.sort(key=lambda x:(x[1],x[0]))

lastEd = 0
score = 0
for conf in confs:
    st,ed = conf
    if st >= lastEd:
        score += 1
        lastEd = ed
print(score)