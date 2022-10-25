def solution():
    n, m = map(int, input().split(" "))
    min_cnt = 999
    chess = []
    chess_range = []
    for i in range(n):
        chess.append(list(input()))

    for i in range(n-7):
        for j in range(m-7):
            chess_range.append((i, i+8, j, j+8))

    for chess_ran in chess_range:
        cnt_w_start = 0
        cnt_b_start = 0
        for i in range(chess_ran[0], chess_ran[1]):
            for j in range(chess_ran[2], chess_ran[3]):
                if (i+j)% 2 == 0:
                    if chess[i][j]!= "W":
                        cnt_w_start += 1
                    if chess[i][j]!="B":
                        cnt_b_start += 1

                if (i+j)%2 == 1:
                    if chess[i][j] != "W":
                        cnt_b_start += 1
                    if chess[i][j] != "B":
                        cnt_w_start += 1
        if min_cnt > min(cnt_w_start, cnt_b_start):
            min_cnt = min(cnt_w_start, cnt_b_start)
    return min_cnt

print(solution())