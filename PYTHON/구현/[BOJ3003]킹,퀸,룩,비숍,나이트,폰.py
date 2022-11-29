def check_piece_number(piece_number: list) -> str:
    result_number = [1, 1, 2, 2, 2, 8]
    for i in range(len(result_number)):
        result_number[i] = result_number[i] - piece_number[i]
    return " ".join(map(str, result_number))

if __name__ == "__main__":
    piece_number = list(map(int, input().split(" ")))
    print(check_piece_number(piece_number))

