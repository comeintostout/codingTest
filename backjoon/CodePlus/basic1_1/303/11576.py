import sys
input = sys.stdin.readline

[A,B]= map(int,input().rstrip().split())
m = int(input())

listA = list(map(int,input().rstrip().split()))
base10 = 0

jinsu = 1
while len(listA) > 0:
    base10 += (jinsu * listA.pop())
    jinsu *= A

listB = []
while base10 > 0:
    listB.append(str(base10 % B))
    base10 = int(base10/B)

print(" ".join(listB[::-1]))