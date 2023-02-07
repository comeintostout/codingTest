N = int(input().rstrip())
numbers = list(map(int, input().rstrip().split()))

sosu = 0
for number in numbers:
    if number == 1:
        continue
    count = 0
    for k in range(2,number):
        if number % k == 0:
            count += 1
    if count == 0:
        sosu += 1

print(sosu)