[N,M] = map(int,input().rstrip().split())

def printList(origin, pickedList, pick):
    if pick == 0:
        print(" ".join(pickedList))
        return
    
    for i in range(len(origin)):
        tmpOrigin = [origin[_] for _ in range(i,len(origin))]
        tmpPickedList = [_ for _ in pickedList]
        tmpPickedList.append(str(tmpOrigin[0]))
        printList(tmpOrigin,tmpPickedList,pick-1)

listN = [i for i in range(1,N+1)]
printList(listN,[],M)
