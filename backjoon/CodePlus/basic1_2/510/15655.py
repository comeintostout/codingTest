[N,M] = map(int,input().rstrip().split())
A = list(map(int,input().rstrip().split()))

A.sort()

def printList(origin, pickedList, pick):
    if pick == 0:
        print(" ".join(pickedList))
        return
    
    for i in range(len(origin)):
        tmpOrigin = [origin[j] for j in range(i,len(origin))]
        tmpPickedList = [_ for _ in pickedList]
        tmpPickedList.append(str(tmpOrigin.pop(0)))
        printList(tmpOrigin,tmpPickedList,pick-1)

printList(A,[],M)