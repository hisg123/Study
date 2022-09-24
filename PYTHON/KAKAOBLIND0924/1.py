def subtractDate(fromdate, todate):
    from_list = list(map(int, fromdate.split(".")))
    to_list = list(map(int, todate.split(".")))

    years = (from_list[0]- to_list[0])
    months = (from_list[1] - to_list[1])
    days = from_list[2] - to_list[2]

    return days + months*28 + years*12*28

def makeDict(terms):
    terms_dict = {}
    for term in terms:
        terms_dict[term[0]] = int(term[1:len(term)])
    return terms_dict

def solution(today, terms, privacies):
    answer = []

    terms_dict = makeDict(terms)
    cnt = 1
    for privacy in privacies:
        todate, type = privacy.split(" ")
        # print(todate, subtractDate(today, todate), terms_dict[type]*28)
        if terms_dict[type]*28 <= subtractDate(today, todate):
            answer.append(cnt)
        cnt += 1

    return answer

today = "2022.05.19"
terms = ["A6", "B12", "C3"]
privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]

print(solution(today, terms, privacies))