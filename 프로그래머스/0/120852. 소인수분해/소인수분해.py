def solution(n):
    answer = []
    while n>1:
        for i in range(2,n+1):
            if n%i ==0:
                n = n//i             
                answer.append(i)
                break

    answer = list(set(answer))
    answer.sort()
    return answer