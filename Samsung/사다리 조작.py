N, M, H = map(int, input().split())
visited = [[False] * (N+1) for _ in range(H+1)]
candidates = []

for _ in range(M):
    h, n = map(int, input().split())
    visited[h][n] = True

def check():
    for n in range(1, N+1): # 내려올 애들
        now = n
        for h in range(1, H+1): # 내려오는 층
            if visited[h][now]: # 현재 위치가 True면 오른쪽 한 칸
                now += 1
            elif visited[h][now-1]:  # 현재 위치에서 n-1에 있는 애가 있으면 왼쪽 한 칸 (0이 나와도 어차피 False라 상관 X)
                now -= 1
        if now != n:
            return False
    return True

# 모든 곳을 방문하는 dfs => 후보들에 대한 모든 경우의 수를 해보는데 depth가 answer보다 큰 경우는 더 안감.
def dfs(depth, start_i):    # dfs는 answer랑 visited만 조작할 뿐 return X
    global answer
    if depth >= answer: # depth가 answer보다 크면 안해. (최소의 depth인 answer를 찾는 것이기 때문)
        return
    if check(): # depth를 answer에 할당.
        answer = depth
        return

    for cnd_i in range(start_i, len(candidates)):    # 후보들 중 안 지나온 곳 다 dfs
        h, n = candidates[cnd_i]    # cnd_i 번째 후보
        if not visited[h][n-1] and not visited[h][n+1]:   # 양 옆에 사다리 없어야 가로선 추가 가능
            visited[h][n] = True
            # True로 바꾸고 depth가 깊어짐. # 깊어지고 나서 밑에 dfs에서 check해줌. # 추가된 가로선 개수
            # 다음꺼부터 돌리려면 cnd_i + 1 해야지
            dfs(depth + 1, cnd_i + 1)
            visited[h][n] = False # dfs 다 돌고 정답이 있든 없든 다음 depth = 0부터 다시 돌아야하기 때문에


# 후보 만들기
# * 현재 위치 (h, n)에서 (h, n-1) 이나 (h, n+1)가 True면 후보 제외
for h in range(1, H+1):
    for n in range(1, N):   # N은 줄 못 놓음. N-1까지 가능
        if not visited[h][n] and not visited[h][n-1] and not visited[h][n+1]:
            candidates.append([h, n])

# dfs 돌리기
answer = 4  # 초기는 4로 둠. 왜냐면 depth >= answer면 끝내버리니까 글고 3까지만 돌려야 하니까 4보다 커지면 안 돌아가게 끔.
dfs(0, 0)   # idx=0인 candidate부터 depth=0부터 시작.

print(-1 if answer >= 4 else answer)
