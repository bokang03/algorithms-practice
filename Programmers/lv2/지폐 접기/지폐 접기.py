def solution(wallet, bill):
    answer = 0

    while True :
        if min(wallet) >= min(bill) and max(wallet) >= max(bill) :
            return answer
        else :
            bill[bill.index(max(bill))] = max(bill)//2
            answer += 1

    return bill