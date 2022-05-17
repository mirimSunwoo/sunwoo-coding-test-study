def solution(arr, divisor):
    answer = []
    for x in arr:
        if x%divisor == 0:
            print(x)
            answer.append(x)
    if len(answer) == 0:
        answer.append(-1)
    answer = sorted(answer)
    return answer

#다른사람의 풀이
def solution(arr, divisor): return sorted([n for n in arr if n%divisor == 0]) or [-1]
