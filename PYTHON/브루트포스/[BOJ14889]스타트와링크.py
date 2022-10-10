from itertools import combinations

def solution():
    n = int(input())
    s = []
    sum_dict = {}

    for i in range(n):
        s.append(list(map(int, input().split(" "))))
    print(s)

    index_list = combinations([i for i in range(n)], n//2)

    for index in index_list:
        print(index)

    return
    for i in range(n):
        for j in range(n):
            if i != j:
                sum_dict[(i,j) if j > i else (j,i)] = s[i][j] + s[j][i]

    print(sum_dict)
    min_sum = 999
    for key in sum_dict:
        selected = []
        selected.append(key[0])
        selected.append(key[1])
        for key2 in sum_dict:
            for key2_val in key2:
                if not key2_val in selected:
                    if min_sum > abs(sum_dict[key] - sum_dict[key2]):
                        min_sum = abs(sum_dict[key] - sum_dict[key2])
                        print(key, key2, selected, sum_dict[key], sum_dict[key2])
                else: break
    print(min_sum)
    # print(list(combinations(sum_dict, n//2)))
    # print(list(combinations(sum_dict.values(), n//2)))

    return

if __name__ == "__main__":
    solution()