def solution(arr1, arr2):            # 2차원 행렬을 잘 이해해보자 그러면 i와 j가 어떻게 쓰이는지 확인할 수 있다. 
    for i in range (len(arr1)):      # i는 arr1의 첫번째 행 과 두번째 행을 비교할 수 있다. 
        for j in range (len(arr1[0])):    # j는 arr1내에 첫번째 열과 두번 째 열을 비교할 수 있다.
            arr1[i][j] += arr2[i][j]      # 두 리스트는 구조가 동일함으로 i,j를 사용하여 arr1에 더하기
    return arr1
