"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None
        visited = [False]*101
        stack = [(node, Node(node.val))]
        visited[1] = stack[0][1]
        while(stack):
            node, new_node = stack.pop()
            for neib in node.neighbors:
                if not visited[neib.val]:
                    new_neib = Node(neib.val)
                    visited[neib.val] = new_neib
                    stack.append((neib, new_neib))
                else:
                    new_neib = visited[neib.val]
                new_node.neighbors.append(new_neib)
            
        return visited[1]
