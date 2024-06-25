from itertools import permutations    # itertools의 수열을 사용하기 위한 전처리


def solution(k, dungeons):
    answer = 0
    
    for p in permutations(dungeons, len(dungeons)):        # 수열(리스트명, 리스트 내 원자 수)
        fatigue = k                                        # 현재 피로도
        cnt = 0                                            # 던전 횟수
        
        for need, spend in p:                              # 반복 필요피로도, 사용피로도가 p만큼 존재
            if fatigue >= need:                            # 조건 필요피로도가 피로도보다작을때
                fatigue -= spend                           # 사용피로도를 빼줌
                cnt += 1                                   # 던전횟수 1 증가
        answer = max(answer,cnt)                           # 반복을 통해서 던전 한 횟수가 최대가 되는 경우의 수를 구함
    
    
    return answer
