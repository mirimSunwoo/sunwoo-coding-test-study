def solution(phone_book):
    #내가 시도한 방법
    answer = True
    for i in (0,len(phone_book)):
        num_len = len(phone_book[i])-1
        if phone_book[i] == phone_book[i+1][:num_len]:
            print(phone_book[i+1][:num_len])
            answer = True
        else:
            print(phone_book[i+1][:num_len])
            answer = False
    return answer

    #내코드에 another코드를 접목한것
    answer = True
    phone_book.sort()
    for i in range(0,len(phone_book)-1):
        if len(phone_book[i]) < len(phone_book[i+1]):
            if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
                answer = False
                break
    return answer

# 다른사람의 풀이
def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True