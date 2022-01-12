'''
8
이름에 특정 문자가 포함된 개수 구하기
대조영빌딩
4F  Kickboard Association
3F  Common Engineering
2F  Adios
1F  CafeMasita. Ltd
회사 이름에 'A' 또는 'K'가 들어가는 회수 세기
'''
def solution(name_list):
    answer = 0
    for name in name_list:
        for char in name:
            if char.find('A') != -1 or char.find('K'):
                answer += 1
                break
    return answer

print('8번',solution(['korea','8층에 사는 선미씨','8번 효정이']))