def solution(array):
    answer = 0
    tmp_key = set(array)
    counter = [0]*1000
    for i in tmp_key:
        for j in array:
            if i == j:
                counter[i] += 1
    answer = counter.index(max(counter))
    if counter.count(max(counter))>1:
        return -1

        
    return answer