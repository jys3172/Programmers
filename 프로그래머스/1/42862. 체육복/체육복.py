def solution(n, lost, reserve):
    set_lost = set(lost) - set(reserve)        # set함수 이해하기(중복x, 순서x)
    set_reserve = set(reserve) - set(lost)     # 문제를 이해, 여분옷이 있는 사람도 도난 가능, 그러므로 set(데이터를 쉽게 제거, 추가, 비교 할 수 있음)을 이용하여 lost와 reserve에 같이 존재하는 데이터 제거
    
    for i in set_reserve:
        if i-1 in set_lost:            # 왼쪽 사람이 빌려주고
            set_lost.remove(i-1)       # 제거
        elif i+1 in set_lost:          # 오른쪽 사람이 빌려주고
            set_lost.remove(i+1)       # 제거
    
    answer = n - len(set_lost)         # 전체 학생수 - 없는 학생
    return answer
