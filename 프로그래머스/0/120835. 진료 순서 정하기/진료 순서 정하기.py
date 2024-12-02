def solution(emergency):
    answer = []
    tmp = emergency.copy()
    tmp.sort(reverse=True)
    for i in emergency:   
        answer.append(tmp.index(i)+1)
    return answer