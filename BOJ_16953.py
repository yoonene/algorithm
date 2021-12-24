from collections import deque

def solution(a, b):
    queue = deque([(a, 1)])
    while queue:
        n, cnt = queue.popleft()
        if n == b:
            return cnt
        if n*2 <= b:
            queue.append((n*2, cnt + 1))
        if int(str(n) + '1') <= b:
            queue.append((int(str(n)+'1'), cnt + 1))
    return -1

a,b = map(int, input().split())
print(solution(a,b))
