def solution(s):
    answer =''
    center = int(len(s)/2)
    if len(s) % 2 !=0:
        answer = s[center]        
    else:
        answer = s[center-1]+s[center]
    return answer