'''
학습대상자 수를 구하는 함수 구하기
'''
def solution(scores):
    count = 0
    for s in range(len(scores)): #정수가 들어간다(range는 알아서 1을 빼줌)
        if scores[s] <= 200:
            count += 1
    return count

scores = [100,210,300,400,140,199]
print(solution(scores))