# Tip! : Left Editor 와 Right Editor 의 개념으로 접근해보자. 속도가 매우 빨라진다.

import sys
input = sys.stdin.readline

string =  input().rstrip()
linkedList=[]

left = -1
right = 1
for s in string:
    linkedList.append([left,s,right])
    left += 1
    right += 1
linkedList.append([left,'',-1])


M = int(input())
L = len(string)
cursor = L

for _ in range(M):
    query = input().split()
    if query[0] == "L":
        leftIdx = linkedList[cursor][0]
        if leftIdx != -1:
            cursor = leftIdx
    elif query[0] == "D":
        rightIdx = linkedList[cursor][2]
        if rightIdx != -1:
            cursor = rightIdx
    elif query[0] == "B":
        leftIdx = linkedList[cursor][0]
        if leftIdx != -1:
            leftNode = linkedList[leftIdx]
            linkedList[cursor][0] = leftNode[0]
            if leftNode[0] != -1:
                linkedList[leftNode[0]][2] = cursor
            leftNode[0] = leftNode[2] = -1
    else:
        leftIdx = linkedList[cursor][0]
        rightIdx = cursor
        L += 1
        if leftIdx != -1:
            leftNode = linkedList[leftIdx]
            leftNode[2] = L
        if rightIdx != -1:
            rightNode = linkedList[rightIdx]
            rightNode[0] = L

        newNode = [leftIdx, query[1],rightIdx]
        linkedList.append(newNode)


firstNode = 0
for node in linkedList:
    if node[0] == -1 and node[2] != -1:
        firstNode = node
        break

node = firstNode
answer= []
while node[2] != -1:
    answer.append(node[1])
    node = linkedList[node[2]]

print("".join(answer))