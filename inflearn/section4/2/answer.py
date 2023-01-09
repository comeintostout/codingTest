import sys
sys.stdin = open("in5.txt","rt")

[K, N] = list(map(int,input().strip().split(" ")))

lineList = []
for _ in range(0,K):
    lineList.append(int(input().strip()))
lineList.sort()

# 1 range 구하기
maxL = 0
left = 1
right = 1
for line in lineList:
    leftCount = rightCount = 0
    left = right
    right = line

    for j in range(0,len(lineList)):
        leftCount += lineList[j]//left
        rightCount += lineList[j]//right

    if(leftCount > N and rightCount < N):
        break


maxLength = 0
while left < right:
    mid = int((left + right) / 2)
    
    count = 0
    for j in range(0,len(lineList)):
        count += lineList[j]//mid

    if count < N: # 더 짧게
        right = mid - 1
    else:
        maxLength = mid
        left = mid + 1

print(maxLength)