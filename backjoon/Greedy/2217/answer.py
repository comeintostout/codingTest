input = open(0).readline

N = int(input())
lopes = []
answer = []

for i in range(N):
    lopes.append(int(input()))
lopes.sort()

biggest = 0
for i in range(len(lopes)):
    biggest = max(lopes[i]*(N-i),biggest)
print(biggest)