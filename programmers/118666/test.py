def solution(survey, choices):
    answer = ['R','C','J','A']
    points = {
        "R":0,
        "T":0,
        "C":0,
        "F":0,
        "J":0,
        "M":0,
        "A":0,
        "N":0
    }

    for i in range(0,len(choices)):
        if(choices[i] > 4):
            points[survey[i][1]] += choices[i]-4
        elif(choices[i] < 4):
            points[survey[i][0]] += 4-choices[i]
        print(points)       

    if(points["R"] < points["T"]):
        answer[0]="T"
    if(points["C"] < points["F"]):
        answer[1]="F"
    if(points["J"] < points["M"]):
        answer[2]="M"
    if(points["A"] < points["N"]):
        answer[3]="N"

    return ''.join(answer)


print(solution(["AN", "CF", "MJ", "RT", "NA"],[5, 3, 2, 7, 5]))