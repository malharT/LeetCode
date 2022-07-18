class Solution:
    def get_max_height(self, node, visited, edges, heights):
        visited.add(node)
        h_max = None
        second_h_max = None 
        winner = None
        for node2 in edges[node]:
            if node2 not in visited:
                h = self.get_max_height(node2, visited, edges, heights)
                h = h+1
                if h_max is None or h_max < h:
                    second_h_max = h_max
                    h_max = h
                    winner = node2
                elif second_h_max is None or h > second_h_max:
                    second_h_max = h
        if h_max is None:
            h_max = 0
        heights[node] = [h_max, second_h_max, winner]
        return h_max

    def set_max_height(self, node, height, visited, edges, heights, min_max_height_club, min_max_height_lim):
        visited.add(node)
        max_h, second_max_h, winner = heights[node]
        if height is not None:
            if height > max_h:
                winner = None
                max_h = height
            elif second_max_h is None or height > second_max_h:
                second_max_h = height
        if max_h < min_max_height_lim:
            min_max_height_club.clear()
            min_max_height_club.add(node)
            min_max_height_lim = max_h
        elif max_h == min_max_height_lim:
            min_max_height_club.add(node)
        for node2 in edges[node]:
            if node2 not in visited:
                if node2 == winner and second_max_h is not None:
                    self.set_max_height(node2, second_max_h + 1, visited, edges, heights, min_max_height_club, min_max_height_lim)        
                else:        
                    self.set_max_height(node2, max_h + 1, visited, edges, heights, min_max_height_club, min_max_height_lim)


    def findMinHeightTrees(self, n: int, edges):
        if n == 1:
            return [0]
        edges_as_dict = {}
        for edge in edges:
            e0 = edge[0]
            e1 = edge[1]
            if e0 not in edges_as_dict:
                edges_as_dict[e0] = []
            if e1 not in edges_as_dict:
                edges_as_dict[e1] = []
            edges_as_dict[e0].append(e1)
            edges_as_dict[e1].append(e0)
        heights = {}
        h = self.get_max_height(0, set(), edges_as_dict, heights)
        min_max_height_club = set()
        min_max_height_lim = float('inf')
        if heights[0][1] is None:
            self.set_max_height(0, 0, set(), edges_as_dict, heights, min_max_height_club, min_max_height_lim)
        else:
            self.set_max_height(0, None, set(), edges_as_dict, heights, min_max_height_club, min_max_height_lim)
        return list(min_max_height_club)