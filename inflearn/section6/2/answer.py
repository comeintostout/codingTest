def DFS(v):
    if v > 7:
        return
    DFS(v*2)
    DFS(v*2+1)
    print(v,end=" ")

def BFS(v):
    if v > 7:
        return
    BFS(v*2)
    print(v,end=' ')
    BFS(v*2 + 1)

def BFS2(v):
    if v > 7:
        return
    print(v, end = " ")
    BFS2(v*2)
    BFS2(v*2+1)

if __name__ == "__main__":
    print("전위순회 출력      :",end=" ")
    BFS2(1)
    print()

    print("중위순회 출력(BFS) :",end=" ")
    BFS(1)
    print()

    print("후위순회 출력(DFS) :",end=" ")
    DFS(1)
    print()