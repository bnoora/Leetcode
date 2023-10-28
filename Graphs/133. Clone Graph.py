from typing import Optional
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        cloner = {}

        def dfs(node):
            if not node:
                return None
            if node in cloner:
                return cloner[node]
            new_node = Node(node.val)
            cloner[node] = new_node
            for neighbor in node.neighbors:
                new_node.neighbors.append(dfs(neighbor))
            return new_node
        return dfs(node)
        

