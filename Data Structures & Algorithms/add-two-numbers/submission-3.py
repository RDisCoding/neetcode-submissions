# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, l1)
        ptr = dummy
        carry = 0

        while l1 and l2:
            total = (l1.val+l2.val+carry)
            l1.val = total%10
            carry = total//10
            if l1.next and l2.next:
                l1 = l1.next
                l2 = l2.next
            else:
                break
        
        print(l1.val)
        print(l2.val)

        while l1.next:
            l1 = l1.next
            total = carry + l1.val
            l1.val = total%10
            carry = total//10
        
        if l2.next:
            l1.next = l2.next
            l1 = l1.next

        while l2.next:
            l2 = l2.next
            total = carry + l2.val
            l2.val = total%10
            carry = total//10
        
        print(l1.val)
        print(l2.val)
        print(carry)

        if carry and not l1.next and not l2.next:
            l1.next = ListNode(carry, None)
            l1 = l1.next      
        
        return dummy.next



