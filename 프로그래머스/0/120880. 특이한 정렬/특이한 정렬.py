def solution(numlist, n):
    answer = []
    distence = []
    for i in numlist:
        distence.append(i-n)
    distence= sorted(distence, key = abs)

    for j in distence :
        if len(answer) ==0:
            answer.append(j+n)
        elif abs(answer[-1]-n)!= j:
            answer.append(j+n)
        else :
            answer.insert(len(answer)-1,j+n)
        
    return answer