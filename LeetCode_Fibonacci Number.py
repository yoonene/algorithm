# https://leetcode.com/problems/fibonacci-number/
class Solution:
    # 변수 2개
    # 굳이 공간복잡도 O(n) 필요 없이 변수 2개면 피보나치 가능
    def fib(self, n: int) -> int:
        x, y = 0, 1
        for _ in range(n):
            x, y = y, x+y
        return x
