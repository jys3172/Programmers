def solution(str_list, ex):
    # 새로운 리스트 생성
    filtered_list = []
    
    # str_list를 순회하며 ex를 포함하지 않는 문자열을 filtered_list에 추가
    for s in str_list:
        if ex not in s:
            filtered_list.append(s)
    
    # 리스트의 문자열을 하나로 합침
    result = ''.join(filtered_list)
    
    # 결과 문자열 반환
    return result
