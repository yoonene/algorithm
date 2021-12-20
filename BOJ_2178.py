N, M = map(int, input().split())
graph = [list(map(int,input())) for _ in range(N)]

dx = [0,0,-1,1]  # 상하좌우
dy = [1,-1,0,0]

from collections import deque

def bfs(x,y):
    queue = deque([(x,y)])
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<M:
                if graph[nx][ny]==1:
                    queue.append((nx,ny))
                    graph[nx][ny] = graph[x][y] + 1	# 최단 블록 찾을 떈 이렇게 함

    return graph[N-1][M-1]

visited = [[False]*M for _ in range(N)]

print(bfs(0,0))	# print를 꼬옥 써,,
