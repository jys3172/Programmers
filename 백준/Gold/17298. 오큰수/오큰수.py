n = int(input())
ans = [-1] * n  # 초기화를 -1로 해둠 (기본적으로 오큰수가 없는 경우를 처리하기 위함)
A = list(map(int, input().split()))
stack = []

for i in range(n):
    while stack and A[stack[-1]] < A[i]:  # 오큰수 조건
        ans[stack.pop()] = A[i]  # 정답 리스트에 오큰수 저장
    stack.append(i)
    
print(" ".join(map(str, ans)))
