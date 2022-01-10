def sum_list(scores):
    result = 0
    for x in scores:
        result += x
    return result

def max_list(scores):
    max = 0
    for x in scores:
        if x > max:
            max = x
    return max

def min_list(scores):
    min = max(scores)
    for x in scores:
        if x<min:
            min = x
    return min

def avg_list(scores):
    avg = 0
    sum = 0
    for x in scores:
        sum += x
    avg = sum/len(scores)
    return avg

def count_even(scores):
    count = 0
    for x in scores:
        if(x %2 ==0):
            count += 1
    return count

def make_list(number):
    return [0]*number

# 1. 숫자가 들어있는 리스트의 합계
scores = [10, 3, 20, 50]
print(sum_list(scores))   #83
# 2. 최댓값
print(max_list(scores))   #50
# 3. 최솟값
print(min_list(scores))   #3
# 4. 평균
print(avg_list(scores))   #20.75
# 5. 짝수인 것만 세기
print(count_even(scores))   #3
# 6. N개의 0을 가진 리스트 만들기
print(make_list(6))   #[0, 0, 0, 0, 0, 0]