import math
N = int(input())
root = int(math.sqrt(N))+1

divider = 2
while N > 1 and divider <= (root+1):
    if N % divider == 0:
        N = int(N/divider)
        print(divider)
    else:
        divider += 2 if divider != 2 else 1
if N != 1:
    print(N)