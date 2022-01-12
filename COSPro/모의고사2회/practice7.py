'''
7
문자열에서 숫자들을 보수가 되는 숫자로 바꾸려고 합니다.
숫자들의 보수는 두숫자의 ASCII코드 값을 더했을 때 문자 'i'가 되는 관계로 정의합니다.
예를들어 주어진 문자열이 "ab1c3d"라면 ab8c6d라는 문자열을 만들면 됩니다.
'0' --- '9'
'1' --- '8'
'2' --- '7'
'3' --- '6'
'4' --- '5'
한줄 수정하기
'''
def solution(s):
    answer = []
    for c in s:
        if '0' <= c <= '9':
            n = ord(c) - ord('i')
            c = chr(n)
        answer.append(c)
    return ''.join(answer)
