# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next: return None

        fast, slow = head.next, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        mid = slow.next
        slow.next = None

        prev = None

        while mid:
            nxt = mid.next
            mid.next = prev
            prev = mid
            mid = nxt
        
        list1 = head
        list2 = prev

        while list1 and list2:
            nxt1 = list1.next
            nxt2 = list2.next
            list1.next = list2
            list2.next = nxt1
            list1 = nxt1
            list2 = nxt2


        

