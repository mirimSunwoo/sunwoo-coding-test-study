#문자열 내에 지정하는 문자들이 있는지 확인하는 함수 수정하기
def solution(password, key):
    answer = 0
    match_cnt = 0
    for k in key:
        for p in password:
            if k == p:
                match_cnt += 1
                break
    if match_cnt >= len(key):
        answer = 1
    return answer

print(solution('GGGa9##','Ga9#')) #1
print(solution('GGGa##','Ga9#')) #0