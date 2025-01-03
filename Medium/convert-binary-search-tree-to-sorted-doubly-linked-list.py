"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return root
        stack = [(root, False)]
        result = []
        while True:
            if len(stack) == 0:
                break
            current_node, visited = stack.pop()
            if visited:
                if len(result) == 0:
                    # The head
                    result.append(current_node)
                else:
                    ans = result[-1]
                    current_node.left = ans
                    ans.right = current_node
                    result.append(current_node)
            else:
                if current_node.right is not None:
                    stack.append((current_node.right, False))
                stack.append((current_node, True))
                if current_node.left is not None:
                    stack.append((current_node.left, False))
            
        # Link the head and the last
        head = result[0]
        last = result[-1]
        head.left = last
        last.right = head

        return head
            

            

