def solution(seoul):
    # 방법1
    answer = str(seoul.index("Kim"))
    return "김서방은 "+answer +"에 있다"

    # 방법2
    return "김서방은 "+str(seoul.index("Kim"))+"에 있다"