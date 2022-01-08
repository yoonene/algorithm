from itertools import combinations
def solution(numbers):
    comb = combinations(numbers, 2)
    result = []
    for c in comb:
        result.append(sum(c))
        
    result = list(set(result))
    return sorted(result)
