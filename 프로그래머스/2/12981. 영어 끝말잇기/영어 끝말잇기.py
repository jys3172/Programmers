# 다시 풀어보기

def solution(n, words):
    for i in range(1, len(words)):    # 첫번째껀는 비교할 필요 없응므로
        if words[i][0] != words[i-1][-1] or words[i] in words[:i] :        # 두가지 조건 1. 앞단어의 젤 뒤 문자와 현제 단어 젤 앞 단어가 일치하는지, 2. 현재 단어가 이전 단어에 포함이 되는지 (※word[:i]는 이전부터 지금까지의 리스트)
            return [(i%n)+1, (i//n)+1]                                     # 조건을 만족하면 몇번째 사람인지, 몇번째 주기에 중복됬는지 리턴 
    else:
        return [0,0]
    

