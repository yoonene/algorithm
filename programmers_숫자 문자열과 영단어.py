def solution(s):
    nums = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    for i,n in enumerate(nums):
        s = s.replace(n, str(i))
        
    return int(s)
