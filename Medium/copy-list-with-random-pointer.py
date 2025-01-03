"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None

        nodes2indx = dict()
        cn = head
        indx = 0
        while cn is not None:
            nodes2indx[cn] = indx
            cn = cn.next
            indx += 1
        
        indx2nodes = []
        nln = dict()
        fcn = head
        new_head = Node(x=fcn.val)
        ncn = new_head
        indx = 0

        while fcn is not None:
            indx2nodes.append(ncn)
            # pointers
            # random
            if fcn.random is None:
                ncn.random = None
            
            else:
                rand_indx = nodes2indx[fcn.random]
                if rand_indx <= indx:
                    # from indx2nodes
                    rand = indx2nodes[rand_indx]
                    ncn.random = rand
                else:
                    # to nln if not already there
                    if rand_indx in nln:
                        rand = nln[rand_indx]
                    else:
                        rand = Node(x=fcn.random.val) 

                    ncn.random = rand
                    nln[rand_indx] = rand

            # next
            if fcn.next is not None:
                if (indx + 1) in nln:
                    next_node = nln[indx + 1]
                else:
                    next_node = Node(x=fcn.next.val)
            else:
                next_node = None

            ncn.next = next_node
            ncn = next_node
            fcn = fcn.next
            indx += 1
                    
        return new_head



        



        


