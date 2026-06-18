# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        start1 , start2 = head, head
        while start2 and start2.next:
            start1 = start1.next
            start2 = start2.next.next
        print(start1.val)
        partway = start1.next
        start1.next = None

        prev= None
        curr= partway
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        partway = prev

        ptr1, ptr2 = head, partway
        ans = head
        while partway:
            ptr1 = ptr1.next
            head.next = partway
            ptr2 = ptr2.next 
            partway.next = ptr1
            head = ptr1
            partway = ptr2