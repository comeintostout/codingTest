N = input().rstrip()
L = len(N)
N = int(N)

digit = 0
count = 9
for i in range(1,L):
    digit += (i * count)
    count *= 10
count = pow(10,(L-1))
digit += (L*(N-count+1))
print(digit)