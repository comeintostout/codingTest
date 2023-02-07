N = int(input())
res = 1

count = 0
for i in range(5,N+1,5):
    k = i
    while k % 5 == 0:
        count += 1
        k = int(k/5)
print(count)