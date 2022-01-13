#페인트칠하는데 걸리는 시간을 구하는 함수 빈칸 채우기

def solution(walls):
    answer = 0
    painted_walls = 0
    hour = 1
    while painted_walls<walls:
        painted_walls = (hour) + (hour//2) + (hour//4)
        hour += 1
    answer = painted_walls
    return hour -1

print(solution(7)) #4