class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        edges_as_dict = {}
        for edge in edges:
            if edge[0] not in edges_as_dict:
                edges_as_dict[edge[0]] = []
            edges_as_dict[edge[0]].append(edge[1])
            if edge[1] not in edges_as_dict:
                edges_as_dict[edge[1]] = []
            edges_as_dict[edge[1]].append(edge[0])
        visited = [False]*n
        stack = [source]
        while(stack):
            node = stack.pop()
            if node == destination:
                return True
            else:
                visited[node] = True
                nb = edges_as_dict[node]
                for n in nb:
                    if not visited[n]:
                        stack.append(n)
        return False