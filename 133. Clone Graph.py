"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        visited = set()
        if node is None:
            return None
        to_discover = {node.val: node}
        first_cpy_node = Node(node.val)
        copy_nodes = {node.val: first_cpy_node}
        while to_discover.keys():
            key = set(to_discover.keys()).pop()
            node = to_discover[key]
            
            del to_discover[key]
            visited.add(key)
            for neighbor in node.neighbors:
                if neighbor.val not in copy_nodes:
                    copy_nodes[neighbor.val] = Node(neighbor.val)
                    to_discover[neighbor.val] = neighbor
                copy_nodes[node.val].neighbors.append(copy_nodes[neighbor.val])
        return first_cpy_node