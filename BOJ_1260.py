N, R, start = map(int, input().split())

graph = [[] for _ in range(N+1)]

for i in range(R):
    d, r = map(int, input().split())
    graph[d].append(r)
    graph[r].append(d)
    

def dfs(vertex, graph, visited):
    visited[vertex] = True
    print(vertex, end=' ')
    
    graph[vertex].sort()
    for v in graph[vertex]:
        if not visited[v]:
            dfs(v, graph, visited)
            
from collections import deque

def bfs(start, graph, visited):
    queue = deque([start])  # deque 만들 때  시작점 넣으니까 append 노노
    visited[start] = True

    while queue:
        cur = queue.popleft()
        print(cur, end=' ')
        graph[cur].sort()
        for v in graph[cur]:
            if not visited[v]:
                queue.append(v)
                visited[v] = True
                
visited = [False] * (N+1)
dfs(start, graph, visited)
print()
visited = [False] * (N+1)
bfs(start, graph, visited)
