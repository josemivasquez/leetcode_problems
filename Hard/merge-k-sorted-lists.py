# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from heapq import heappop, heappush

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        nlists = []
        for l in lists:
            if l is None: continue
            ls = []
            cn = l
            while cn != None:
                ls.append(cn.val)
                cn = cn.next
            nlists.append(ls)
        
        lists = nlists

        pointers = []
        s = []
        for i, l in enumerate(lists):
            if len(l) == 0: continue
            pointers.append(0)
            heappush(s, (l[0], i))
        
        r = []
        while len(s) > 0:
            v, lsindx = heappop(s)
            r.append(v)
            if pointers[lsindx] == len(lists[lsindx]) - 1:
                continue
            pointers[lsindx] += 1
            heappush(s, (lists[lsindx][pointers[lsindx]], lsindx))
        
        if len(r) == 0:
            return None

        head = ListNode(val=r[0])
        ans = head
        i = 1
        while i < len(r):
            cn = ListNode(val=r[i])
            ans.next = cn
            ans = cn
            i += 1
        
        return head



        

        

        
