# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists: return None
        def merge(l1, l2):
            dummy = ListNode(0)
            ptr = dummy
            
            while l1 and l2:
                if l1.val <= l2.val:
                    ptr.next = l1
                    l1 = l1.next
                else:
                    ptr.next = l2
                    l2 = l2.next
                ptr = ptr.next
            
            if l1: 
                ptr.next = l1
            if l2: 
                ptr.next = l2
            
            return dummy.next

        
        while len(lists)>1:
            a = lists.pop()
            b = lists.pop()

            m = merge(a,b)
            lists.append(m)

        return lists[0]
