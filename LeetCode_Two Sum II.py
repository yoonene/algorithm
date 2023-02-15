from collections import defaultdict
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, num in enumerate(numbers):
            ex = target - num
            idx = bisect.bisect_left(numbers, ex, i+1)
            if idx < len(numbers) and numbers[idx] == ex:
                return [i+1, idx+1]
