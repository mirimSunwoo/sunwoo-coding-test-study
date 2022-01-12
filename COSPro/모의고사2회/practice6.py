'''
6
몸무게가 k보다 큰 사람은 몇 명인지 세기
65, 70, 75, 80, 84
75보다 큰 사람 2명
한줄 수정하기
'''
def solution(weight, k):
    answer = 0
    for w in weight:
        if w > k:
            answer += 1
    return answer

print(solution([65,70,75,80,84],75))
