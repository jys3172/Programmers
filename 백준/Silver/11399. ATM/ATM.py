N =int(input())
A= list(map(int, input().split()))
S = [0]*N

for i in range(1,N):        # i= 바꾸려는 값(현재 값)
    insert_point = i        
    insert_value = A[i]
    for j in range(i-1,-1,-1):       # j= 비교하는 값들(이전 값들)
        if A[j] < A[i]:
            insert_point = j+1
            break
        if j == 0:
            insert_point = 0
    for j in range(i, insert_point, -1):
        A[j] = A[j-1]
    A[insert_point] = insert_value
    
S[0] = A[0]           # 합 배열, 첫 리스트를 같게, A는 입력받은 리스트, S는 출력할 최종 리스트=> 첫번째 값을 같게 만들었다.

for i in range(1, N):
    S[i] = S[i-1] + A[i]        # 두번째 값부턴 이 식을 이용하여 S[i]에 계산
    
sum = 0
for i in range(0,N):
    sum += S[i]
print(sum)
