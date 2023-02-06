# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        queue = deque()
        node = head
        while node is not None:
            queue.append(node.val)
            node = node.next
        
        while len(queue) > 1:
            if queue.popleft() != queue.pop():
                return False
        
        return True
        
