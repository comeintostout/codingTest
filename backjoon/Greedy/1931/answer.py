input = open(0).readline

meetings = []
answer = 0

N = int(input())
for i in range(N):
    meetings.append(list(map(int,input().split())))
meetings.sort(key=lambda x:(x[1],x[0]))

lastEd = -1
pick = 0
for m in meetings:
    st,ed = m
    if st >= lastEd:
        pick+=1
        lastEd = ed

print(pick)
