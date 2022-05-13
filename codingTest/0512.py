def solution(num):
    count = 0
    while True:
        if num == 1 :
            break
        if num%2 == 0 :
            num = num/2
            # print(answer)
        else:
            num = num * 3 + 1
            # print(answer)
        count += 1
    if count >= 500 :
        return -1
    return count

#다른사람의 풀이
def collatz(num):
    for i in range(500):
        num = num / 2 if num % 2 == 0 else num*3 + 1
        if num == 1:
            return i + 1
    return -1