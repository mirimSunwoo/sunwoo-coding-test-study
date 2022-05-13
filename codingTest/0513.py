def solution(price, money, count):
    answer = 0
    sum_p = 0
    for x in range(1,count+1):
        sum_p += price
        answer += sum_p
        # print(x,sum_p, answer)
    if(money - answer < 0):
        return answer - money
    else:
        return 0

#다른사람의 풀이
def solution(price, money, count):
    return max(0,price*(count+1)*count//2-money)