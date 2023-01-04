def solution(s):
    answer = 0

    x = ''
    xCount=0
    otherCount = 0
    for i in range(0,len(s)):
        if(x == ''):
            x = s[i]
            xCount = 1
        else:
            if(x == s[i]):
                xCount += 1
            else:
                otherCount += 1

            if(xCount == otherCount):
                answer += 1
                xCount = otherCount = 0
                x = ''
    if(len(x) > 0):
        answer += 1
    return answer


s= "abracadabra"
print(solution(s))