#카드 게임 승자 알아내는 함수 작성하기
def solution(mho_cards, mhe_cards):
    result = -1
    count = [0,0]
    for i in range(len(mho_cards)):
        if(mho_cards[i] > mhe_cards[i]):
            count[0] += 1
        elif (mho_cards[i] < mhe_cards[i]):
            count[1] += 1
    print(count)
    if count[0] > count[1] :
        result = 1
    elif count[0] < count[1]:
        result = 0
    else:
        result = -1
    return result
import random
mho_cards = list(range(1,13+1))
random.shuffle(mho_cards)
mhe_cards = list(range(1,13+1))
random.shuffle(mhe_cards)
print(solution(mho_cards,mhe_cards))