import math
def isprime(n):
    if n == 1:
        return False                                # False는 반환 x
    else:        
        for i in range(2, int(math.sqrt(n))+1):     # 제곱근까지 -> 9일 때 2,3을 비교해서 나눠떨어질때 소수아님 11일 때 2,3일때 나눠떨어지지 않으므로 소수
            if n%i ==0:    
                return False
        return True

def solution(n):
    answer = 0
    for i in range(1,n+1):
        if isprime(i):
            answer +=1
    return answer
