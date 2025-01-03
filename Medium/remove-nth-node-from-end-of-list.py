# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> 
        Optional[ListNode]:
        l = []
        cn = head
        l.append(cn)
        while cn.next is not None:
            cn = cn.next
            l.append(cn)
        
        target = l[len(l) - n]

        if target == head:
            return target.next
        
        btarget = l[len(l) - n - 1]
        btarget.next = target.next
        return head
        


            
        

