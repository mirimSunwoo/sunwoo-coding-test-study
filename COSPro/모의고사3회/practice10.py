#문자열들을 처리하는 시간 구하는 함수 수정하기
def solution(strings):
    result = 0
    for s in strings:
        length = len(s)
        result += (length//4)
        if length % 4 != 0:
            result += 1
    return result

print(solution("abcdef1234567"))