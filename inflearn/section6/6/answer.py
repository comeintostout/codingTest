import sys

FILE_NAME = "4.txt"
sys.stdin = open("in"+FILE_NAME,"rt")

def DFS(selected,left):
    global cnt
    if left == 0:
        print(" ".join(selected))
        cnt += 1
        return
    
    for i in range(1,N+1):
        tmp = selected[:]
        tmp.append(str(i))
        DFS(tmp,left-1)

if __name__ == "__main__":
    N, M = map(int,input().split())
    cnt = 0
    DFS([],M)
    print(cnt)
