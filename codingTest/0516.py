def solution(absolutes, signs):
    answer = 0
    cnt = 0
    for i in absolutes: #absolutes의 값만큼 i에 넣고 돌려줍니다(4,7,12)
        # for j in range(1,len(absolutes)): #왜 이렇게 2중 for문을 쓰면 안될까요?
        if signs[cnt] == True: #signs cnt[index]가 True일때
            answer += i #i값만큼 누적합 합니다
        elif signs[cnt] == False: #signs cnt[index]가 Flase일때
            answer -= i #i의 음수값을 반환하는 대신 i값만큼 누적빼기 합니다
        cnt += 1 #배열의 index를 하나씩 늘려줍니다
    return answer #결과값을 반환합니다

#다른사람의 풀이
def solution(absolutes, signs):
    return sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs))