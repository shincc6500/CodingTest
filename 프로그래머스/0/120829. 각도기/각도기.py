def solution(angle):
    answer = 0
    if angle in range(0,90):
        return 1
    elif angle == 90:
        return 2
    elif angle in range(91,180):
        return 3
    else:
        return 4