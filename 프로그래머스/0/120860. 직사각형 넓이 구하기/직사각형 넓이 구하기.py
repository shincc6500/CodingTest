def solution(dots):
    x = []
    y = []
    for i in dots:
        a,b = i
        x.append(a)
        y.append(b)
    l = max(x)-min(x)
    h = max(y)-min(y)
    answer = l*h
    return answer