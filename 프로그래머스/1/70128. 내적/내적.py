def solution(a, b):
    answer = 0
    for i in range(len(a)):
        if a==0 or b==0:
            answer += 0
        else:
            answer += a[i]*b[i]
    return answer