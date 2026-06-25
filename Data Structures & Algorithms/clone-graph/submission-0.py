"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None
        m = {}

        def clone(node):
            if node in m:
                return m[node]
            
            m[node] = Node(node.val)
            for n in node.neighbors:
                x = clone(n)
                m[node].neighbors.append(x)
            
            return m[node]
        
        return clone(node)

