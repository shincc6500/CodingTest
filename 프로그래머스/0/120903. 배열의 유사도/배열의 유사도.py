def solution(s1, s2):
    answer = 0
    for i in set(s1):
        if i in s2:
            answer +=1
    return answer