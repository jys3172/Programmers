# 다시 플어보기

def solution(n):
    answer = [0,1]			# F(0)=0, F(1)=1
    for i in range(2,n+1):	# F(n) = (F(n-1) + F(n-2)) % 1234567
        answer.append((answer[i-1] + answer[i-2]) % 1234567) # i 가 마지막을 가르키고 있으므로 제일뒤의 다음과 다다음 거를 더하는 피보나치를 구현
    
    return answer[-1]		# 마지막 결과를 return
