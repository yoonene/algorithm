# 20057번: 마법사 상어와 토네이도

# 밖으로 나간 모래
answer = 0

# 입력
N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

# 시작점
r, c = N//2, N//2

# 좌, 하, 우, 상 방향별 비율의 중심 기준 위치
left = [(1, 1, 0.01), (-1, 1, 0.01), (-2, 0, 0.02), (2, 0, 0.02), (-1, 0, 0.07), (1, 0, 0.07), (0, -2, 0.05), (-1, -1, 0.1), (1, -1, 0.1), (0, -1, -1)]
down = [(-1, -1, 0.01), (-1, 1, 0.01), (0, -2, 0.02), (0, 2, 0.02), (0, -1, 0.07), (0, 1, 0.07), (2, 0, 0.05), (1, -1, 0.1), (1, 1, 0.1), (1, 0, -1)]
right = [(-1, -1, 0.01), (1, -1, 0.01), (-2, 0, 0.02), (2, 0, 0.02), (-1, 0, 0.07), (1, 0, 0.07), (0, 2, 0.05), (-1, 1, 0.1), (1, 1, 0.1), (0, 1, -1)]
up = [(1, 1, 0.01), (1, -1, 0.01), (0, -2, 0.02), (0, 2, 0.02), (0, -1, 0.07), (0, 1, 0.07), (-2, 0, 0.05), (-1, -1, 0.1), (-1, 1, 0.1), (-1, 0, -1)]


def tornado(dr, dc, dir, step):
    global r, c, answer
    for _ in range(step):
        total_sand = 0
        # 중심 이동
        r += dr
        c += dc
        if r < 0 or c < 0:
            break
        # 비율로 이동
        for dx, dy, ratio in dir:
            nr, nc = r + dx, c + dy
            if ratio == -1:
                move_sand = A[r][c] - total_sand
            else:
                move_sand = int(A[r][c] * ratio)
                total_sand += move_sand
            if 0 <= nr < N and 0 <= nc < N:
                A[nr][nc] += move_sand
            else:
                answer += move_sand
        A[r][c] = 0     # 중심 모래 다 날아감

# 이동
# tornado(0, 0, left, 1)
for i in range(1, N+1):
    if i % 2 != 0:  # i만큼 좌, 하로 이동
        tornado(0, -1, left, i)
        tornado(1, 0, down, i)
    else: # 우, 상
        tornado(0, 1, right, i)
        tornado(-1, 0, up, i)

print(answer)
