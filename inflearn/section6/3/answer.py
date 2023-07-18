import sys

FILE_NAME = "2.txt"
sys.stdin = open("in"+FILE_NAME,"rt")

n = int(input())
S = list(range(1,n+1))

def DFS(s, i,pick):
    if len(s) == i:
        print(pick)
    else:
        DFS(s, i+1, pick[:]+ " " + str(s[i]))
        DFS(s, i+1, pick[:])

DFS(S,0,"")