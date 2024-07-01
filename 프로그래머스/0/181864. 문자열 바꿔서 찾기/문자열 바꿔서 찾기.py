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

## 리스트로 형성한 후 
        - for문확인 mystring을 그냥 넣고 실행가능
        - 리스트를 문자열로 변환하는 방법 -> 위식은 각 리스트마다 ''을 삽입(여백 x)
        ex) ",".join('abcd) -> 'a,b,c,d' 문자열 삽입
        
