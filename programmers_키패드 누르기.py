from collections import deque
def solution(numbers, hand): 
    # 왼손으로 누를 것: n%3 == 1
    # 오른손: n%3 == 0
    # 들어온 순서대로 위의 조건에 따라 1이 나머지면 왼손이 따라가고//
    result = ''
    mtrx = [(3,1),(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
    left = (3,0)
    right = (3,2)
    for n in numbers:
        ld = abs(mtrx[n][1] - left[1]) + abs(mtrx[n][0] - left[0])
        rd = abs(mtrx[n][1] - right[1]) + abs(mtrx[n][0] - right[0])
        if n%3 == 1:
                # for j in range(ld):
                result += 'L'
                left = mtrx[n]
        elif n%3 == 2 or n == 0:
            if ld > rd:
                # for j in range(rd):
                result += 'R'
                right = mtrx[n]
            elif ld < rd:
                # for j in range(ld):
                result += 'L'
                left = mtrx[n]
            elif ld == rd:
                if hand == "right":
                    # for j in range(rd):
                    result += 'R'
                    right = mtrx[n]
                else:
                    # for j in range(ld):
                    result += 'L'
                    left = mtrx[n]
        else:
            # for j in range(rd):
                result += 'R'
                right = mtrx[n]
    return result
