def solution(myString, pat):
    # 변환된 문자열을 저장할 리스트
    transformed = []
    
    # myString을 순회하면서 변환
    for char in myString:
        if char == 'A':
            transformed.append('B')
        elif char == 'B':
            transformed.append('A')
    
    # 리스트를 문자열로 변환
    transformed_str = ''.join(transformed)
    
    # pat이 변환된 문자열에 있는지 확인
    if pat in transformed_str:
        return 1
    else:
        return 0
