import sys

FILE_NAME = "5.txt"
sys.stdin = open("in"+FILE_NAME,"rt")

def DFS(selected):
    global N, M, cnt
    if len(selected) == M:
        print(" ".join(selected))
        cnt += 1
        return

    for i in range(1,N+1):
        if str(i) not in selected:
            tmp = selected[:]
            tmp.append(str(i))
            DFS(tmp)

if __name__ == "__main__":
    cnt = 0
    N, M = map(int,input().split())
    DFS([])
    print(cnt)