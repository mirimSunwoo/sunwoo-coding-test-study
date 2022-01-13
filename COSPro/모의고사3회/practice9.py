#각팀의 총 승점을 구하는 함수 수정하기
def solution(scores):
    result = [0,0,0,0]
    for i in range(4):
        for k in range(4):
            if i != k:
                result[i] += scores[i][k] * 2
        return result

scores = [
    [-1,1,0,0],
    [0,-1,0,1],
    [1,1,-1,1],
    [1,0,0,-1]
]
print(solution(scores))