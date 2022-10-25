def solution():
    n = int(input())
    wt_array = []
    cnt_array = [1 for _ in range(n)]
    for i in range(n):
        wt_array.append(list(map(int, input().split(" "))))

    for i in range(n):
        for j in range(n):
            # print(wt_array[i], wt_array[j])
            if wt_array[i][0] < wt_array[j][0]:
                if wt_array[i][1] < wt_array[j][1]:
                    cnt_array[i] += 1

    return " ".join(map(str, cnt_array))

if __name__ == "__main__":
    print(solution())