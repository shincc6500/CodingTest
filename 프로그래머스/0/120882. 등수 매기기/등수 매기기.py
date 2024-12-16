def solution(score):
    answer = []
    average = []
    rank ={}
    for i in score:
        average.append(sum(i)/len(i))
    for i in average:
        rank[i] = 1
    for i in set(average):
        for j in average:
            if j>i:
                rank[i] += 1
    for i in average:
        answer.append(rank[i])
    return answer