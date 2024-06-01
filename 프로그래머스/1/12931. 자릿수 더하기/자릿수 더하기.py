def solution(n):
    answer = 0
    while n >0:
        answer += n % 10
        n //= 10 -> 나누기 확ㅇ니 잘하기

    return answer
    -> 전반적인 오류는 while문은 잘 사용했지만 내부에서 값을 아예 나누는 생각을 못했음.
