'''
10
ISBN 규칙 확인 하는 함수
국제표준도서번호 ISBN
13자리
첫3자리는 978 또는 979
마지막 1자리의 숫자는 확인 숫자
확인숫자를 제외한 나머지 각 자리마다 가중치를 곱한 값을 더한 총합을 구한다
가중치 1, 3, 1, 3, 1, 3, ...
예
ISBN: 9788960777330
1x9 + 3x7 + 1*8 + 3x8 + 1x9 + 3x6 + 1x0 + 3x7 +1x7 + 3x7 + 1x3 + 3x3
= 150
총합을 10으로 나눈 나머지는 0이므로 10-0은 10이고 규칙에 따라 10일 때는 0으로 계산
즉 마지막 숫자는 0
'''
def sum_isbn(isbn):
    sum=0
    for i in range(len(isbn)):
        c = int(isbn[i])
        if i % 2:
            w = 3
        else:
            w = 1
        sum+=w*c
    return sum
def soulution(isbn):
    answer=''
    total = sum_isbn(isbn)
    answer = 10 - (total % 10)

    if answer == 10:
        answer = 0
    return answer

print(soulution('978896077773300'))