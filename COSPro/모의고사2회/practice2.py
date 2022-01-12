#축구화 주문 수량 구하는 함수 완성하기
def solution(shoes_size):
    size = ["7","7.5","8","8.5","9","9.5"]
    count_size = [0,0,0,0,0,0]
    for index,x in enumerate(size):
        for y in shoes_size:
            if x == y:
                count_size[index] += 1
    return count_size

print(solution(["7","7","8.5","8.5","9","9.5","9.5"]))