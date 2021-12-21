N,M,K = map(int,input().split())

graph = [[0]*M for _ in range(N)]

for i in range(K):
    x, y = map(int, input().split())
    graph[x-1][y-1] = 1
    
dx = [0,0,-1,1]
dy = [1,-1,0,0]
    
from collections import deque

def bfs(x,y):
    queue = deque([(x,y)])
    visited[x][y] = True
    cnt = 1
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<N and 0<=ny<M:
                if not visited[nx][ny] and graph[nx][ny] == 1:
                    queue.append((nx, ny))
                    visited[nx][ny] = True
                    cnt += 1
                    
    return cnt

visited = [[False] * M for _ in range(N)]

trash = []
for n in range(N):
    for m in range(M):
        if not visited[n][m] and graph[n][m]:
            trash.append(bfs(n,m))
            
print(max(trash))
