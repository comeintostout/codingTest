import sys
sys.stdin = open("in5.txt","rt")
from collections import deque

N = int(input())
numbers = deque(map(int,input().split()))

lastNumber = 0
Pick = ""
while numbers:
    if numbers[0] >= numbers[-1]:
        if numbers[-1] > lastNumber:
            lastNumber = numbers.pop()
            Pick += 'R'
        elif numbers[0] > lastNumber:
            lastNumber = numbers.popleft()
            Pick += 'L'       
        else:
            break
    else:
        if numbers[0] > lastNumber:
            lastNumber = numbers.popleft()
            Pick += 'L'
        elif numbers[-1] > lastNumber:
            lastNumber = numbers.pop()
            Pick += 'R'       
        else:
            break
print(len(Pick))
print(Pick)