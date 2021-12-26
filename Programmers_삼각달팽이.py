def solution(n):
    triangle = [[0 for _ in range(i+1)] for i in range(n)]
    x,y = -1, 0
    num = 1
    
    for i in range(n):
        for j in range(n-i):
            if i%3 == 0: #하
                x += 1
            elif i%3 == 1: #중
                y += 1
            else: # 상
                x -= 1
                y -= 1
            triangle[x][y] = num
            num += 1
        
    return sum(triangle, [])
