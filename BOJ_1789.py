# 1789. 수들의 합
"""
[문제] 
서로 다른 N개의 자연수의 합이 S라고 한다. S를 알 때, 자연수 N의 최댓값은 얼마일까?
"""

S = int(input())
cnt = 0
sub = 1

while S > 0:
    S -= sub
    sub += 1
    cnt += 1

if S != 0:
    cnt -= 1
    
print(cnt)
