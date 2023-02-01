def getAnswer(n):
    if n <= 0:
        return 1
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        if answer[n] != 0:
            return answer[n]
        else:
            answer[n] = getAnswer(n-1) +  getAnswer(n-2) +  getAnswer(n-3)
            return answer[n]

answer = [0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0]

tc = int(input())
for i in range(tc):
    n = int(input())
    print(getAnswer(n))

