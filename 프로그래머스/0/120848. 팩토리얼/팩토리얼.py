def solution(n):
    tmp = 1
    for i in range(2,11):
        tmp *= i
        if tmp==n:
            return i
        elif tmp>n:
            return i-1