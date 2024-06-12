def solution(left, right):
    answer = 0;
    for i in range(left,right+1):
        remain = 0;        -> 초기화 장소를 잘 확인하자
        for j in range(1,i+1):
            if(i%j==0):
                remain +=1
        if (remain%2==0):
            answer = answer + i
        else:
            answer = answer -i
    return answer
