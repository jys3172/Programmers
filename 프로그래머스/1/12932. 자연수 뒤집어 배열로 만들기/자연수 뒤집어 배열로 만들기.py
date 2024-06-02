def solution(n):
    answer = []
    s = reversed(str(n)) -> reversed함수 기억하기. 그리고 입력이 12345이므로 n을 string화
    for i in s:
        answer.append(int(i)) -> s는 string이므로 거꾸로 된 첫번째부터 int로 가져옴
    return answer
