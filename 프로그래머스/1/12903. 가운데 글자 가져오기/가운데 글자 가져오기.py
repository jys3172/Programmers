def solution(s):
    answer =''
    center = int(len(s)/2)    -> len()을 사용한다고 형식이 변하지 않는다. 정확히 int를 이용한 형변환
    if len(s) % 2 !=0:
        answer = s[center]        
    else:
        answer = s[center-1]+s[center]
    return answer
