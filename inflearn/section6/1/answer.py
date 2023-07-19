import sys

FILE_NAME = "5.txt"
sys.stdin = open("in"+FILE_NAME,"rt")

def DFS(num):
    if num == 0:
        return
    else:
        DFS(num//2)
        print(num%2, end="")

if __name__ == "__main__":
    n = int(input())
    DFS(n)
    print()