def solution(board):
    answer = 0
    n = len(board)
    
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                for a in range(max(0,i-1),min(n,i+2)):
                    for b in range(max(0,j-1),min(n,j+2)):
                        if board[a][b] != 1:
                            board[a][b] = 2

    for i in board:
        answer += i.count(0)
                            
    return answer