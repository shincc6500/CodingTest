def solution(dots):
    answer = 0
    tmp = []
    x1,y1 = dots.pop()
    for i in range(3):
        tmp = dots.copy()
        x2,y2 = tmp.pop(i)
        x3,y3 = tmp[0]
        x4,y4 = tmp[1]
        if (x1-x2)/(y1-y2) == (x3-x4)/(y3-y4):
            return 1        
    return answer