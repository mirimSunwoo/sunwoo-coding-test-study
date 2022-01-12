'''
9
제품 포장을 위한 포장 상자의 개수 구하기
모든 제품의 높이는 같고 가로세로 길이가 정사각형의 제품 정해진 규격은
1x1, 2x2, 3x3, 4x4, 5x5, 6x6 크기의 제품만 생산
각 규격 크기가 나열된 곳에 필요한 수량을 적음

0, 0, 4, 0, 0, 1
이러면 3x3 4개, 6x6 1개 필요하단 얘기

소포상자의 가로세로 크기는 6x6
위와 같이 주문하면(3x3 4개, 6x6 1개)
소포상자 6x6이 2개가 필요
'''
def solution(orders):
    answer = 0
    size = 0
    for o in orders:
        for i in range(6):
            if o[i]!=0:
                size+=((i+1)**2)*(o[i])
    answer=size//36
    if size % 36 != 0:
        answer += 1
    return answer

print(solution([3,3,3,3,6]))