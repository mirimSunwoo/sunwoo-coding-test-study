def solution(numbers):
    answer = [0,1,2,3,4,5,6,7,8,9]
    sum_answer = sum(answer)
    num_sum = 0
    for i in numbers:
        num_sum += i
    return sum_answer - num_sum

#다른사람의 풀이
def solution(numbers):
    return 45 - sum(numbers) #45숫자가 바뀐다면 비효율적