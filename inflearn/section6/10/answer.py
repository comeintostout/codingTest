import sys
sys.stdin = open("in5.txt","rt")

def DFS(depth):
    global N,M,array,cnt

    if depth == M:
        print(" ".join(array))
        cnt += 1
        return

    st = 1 if depth == 0 else int(array[-1])+1
    for i in range(st,N+1):
        array.append(str(i))
        DFS(depth+1)
        array.pop()


if __name__ == "__main__":
    N, M = map(int,input().split())
    array = []
    cnt = 0
    DFS(0)
    print(cnt)
