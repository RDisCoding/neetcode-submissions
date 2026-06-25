# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ahead = head
        for i in range(n):
            ahead = ahead.next
        curr = head
        
        if not ahead:
            return curr.next

        while ahead.next:
            curr = curr.next
            ahead = ahead.next
        
        if curr.next:
            curr.next = curr.next.next

        return head