def solution(answers):
    spz1 = [1,2,3,4,5]
    spz2 = [2,1,2,3,2,4,2,5]
    spz3 = [3,3,1,1,2,2,4,4,5,5]
    
    [1,2,3,4,5,6,7,8,9,10]
    
    scores = [0, 0, 0]
    n = len(answers)
    
    for i in range(len(answers)):
        if spz1[i%5] == answers[i]:
            scores[0] += 1
        if spz2[i%8] == answers[i]:
            scores[1] += 1
        if spz3[i%10] == answers[i]:
            scores[2] += 1
    
    best = max(scores)
    result = []
    
    for i in range(3):
        if best == scores[i]:
            result.append(i+1)
            
    return result
