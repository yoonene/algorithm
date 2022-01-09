from itertools import permutations

data = ['0','1','2','3','4','5','6','7','8','9']
num = list(permutations(data,3))

N = int(input())

for _ in range(N):
    removed = 0
    n, s, b = input().split()
    for i in range(len(num)):
        strike, ball = 0, 0
        i -= removed
        for j in range(3):
            if n[j] == num[i][j]:
                strike += 1
            elif n[j] in num[i]:
                ball += 1
        if (strike != int(s)) or (ball != int(b)):
            num.remove(num[i])
            removed += 1
            
print(len(num))

# 실패임. 뭐가 
