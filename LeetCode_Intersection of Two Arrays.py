class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = set()
        nums2.sort()
        for num in nums1:
            idx = bisect.bisect_left(nums2, num)
            if idx < len(nums2) and nums2[idx] == num:
                result.add(num)
        
        return result    
