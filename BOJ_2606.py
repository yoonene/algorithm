N = int(input())
R = int(input())

graph = [[] for _ in range(N+1)]

for i in range(R):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
visited = [False for _ in range(N+1)]

def dfs(start):
    cur = start
    visited[cur] = True
    
    for v in graph[cur]:
        if not visited[v]:
            dfs(v)

dfs(1)

print(visited.count(True)-1)
