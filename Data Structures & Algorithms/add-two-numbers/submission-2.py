# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        if not l1: return l2
        if not l2: return l1

        dummy = ListNode(0)
        ans = dummy
        total = 0
        c = 0
        while l1 and l2:
            total = l1.val + l2.val + c
            c = total//10
            ans.next = ListNode(total%10)
            ans = ans.next
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            total = l1.val + c
            c = total//10
            ans.next = ListNode(total%10)
            ans = ans.next
            l1 = l1.next

        while l2:
            total = l2.val + c
            c = total//10
            ans.next = ListNode(total%10)
            ans = ans.next
            l2 = l2.next
        
        if c:
            ans.next = ListNode(c)
            ans = ans.next        
        final = dummy.next
        return final