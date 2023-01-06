import sys
sys.stdin = open("in5.txt","rt")

[N, M] = list(map(int,input().strip().split(" ")))
numberList = list(map(int,input().strip().split(" ")))
numberList.sort()

print(numberList.index(M) + 1)