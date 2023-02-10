# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == []:
            return []
        lst = []
        node = head
        while node is not None:
            lst.append(node.val)
            node = node.next
        
        lst.sort()
        answer_lst = ListNode(0)
        result = answer_lst
        for num in lst:
            answer_lst.next = ListNode(num)
            answer_lst = answer_lst.next
        return result.next
