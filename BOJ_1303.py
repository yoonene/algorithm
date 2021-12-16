from collections import deque
N, M = map(int, input().split())
graph = [list(input()) for _ in range(M)]
visited = [[False] * N for _ in range(M)]

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def bfs(x,y,color):
    cnt = 0
    queue = deque([(x,y)]) # 시작점에 대한 입력 및 방문 처리
    visited[x][y] = True
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<=nx<M and 0<=ny<N:	# 여기서 틀렸었음. 생각 잘하자~
                if  graph[nx][ny] == color:
                    if not visited[nx][ny]:
                        cnt += 1
                        queue.append((nx,ny))
                        visited[nx][ny] = True
                
    return cnt + 1

w_power, b_power = 0, 0

for m in range(M):
    for n in range(N):
        if graph[m][n] == 'W' and not visited[m][n]:
            w_power += bfs(m,n,'W')**2
        elif graph[m][n] == 'B' and not visited[m][n]:
            b_power += bfs(m,n,'B')**2
print(w_power, b_power)
