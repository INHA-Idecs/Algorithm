'''
한 번호가 다른 번호의 접두어인 경우가 있는지 확인
접두어인 경우가 있으면 False 아니면 true
'''

# 성공
def solution(phone_book):
    book = sorted(phone_book)
    for i in range(len(book)-1):
        if book[i] == book[i+1][:len(book[i])]:
            return False
    return True

# 내장함수 쓰면
def solution(phone_book):
    book = sorted(phone_book)
    for i in range(len(book)-1):
        if book[i+1].startswith(book[i]):
            return False
    return True

# 처음 코드 (효율성 테스트 실패)
def solution(phone_book):
    answer = True
    book = sorted(phone_book)
    for i in range(len(book)):
        num = book[i]
        for j in range(i+1, len(book)):
            if num == book[j][:len(num)]:
                answer = False
                break
    return answer

# 이중 중첩문 빠져나오기 (2개 시간초과)
def solution(phone_book):
    answer = True
    book = sorted(phone_book)
    for i in range(len(book)):
        num = book[i]
        for j in range(i+1, len(book)):
            if num == book[j][:len(num)]:
                answer = False
                break
        if answer == False:
            break
    return answer

# 내장함수 이용 (시간초과 ㅠㅠ)
def solution(phone_book):
    answer = True
    book = sorted(phone_book)
    for i in range(len(book)):
        for j in range(i+1, len(book)):
            if book[j].startswith(book[i]):
                answer = False
                return answer
    return answer