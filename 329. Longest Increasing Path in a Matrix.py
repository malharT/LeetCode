class Solution:
    def check_node_and_update(self, i,j, oi, oj, matrix, stack, not_visited):
        if matrix[oi][oj] < matrix[i][j]:
            if (oi, oj) in not_visited:
                stack.append((oi, oj))
    def longestIncreasingPath(self, matrix) -> int:
        not_visited = set()
        stack = []
        dp = []
        max_path = 1
        for i in range(len(matrix)):
            dp.append([1]*len(matrix[0]))
            for j in range(len(matrix[0])):
                not_visited.add((i, j))
        while not_visited or stack:
            if not stack:
                stack.append(not_visited.pop())
                not_visited.add(stack[-1])
            node = stack[-1]
            i = node[0]
            j = node[1]
            if node in not_visited:
                not_visited.remove(node)
                i = node[0]
                j = node[1]
                if i > 0:
                    self.check_node_and_update(i, j, i-1, j, matrix, stack, not_visited)
                if j > 0:
                    self.check_node_and_update(i, j, i, j-1, matrix, stack, not_visited)
                if i + 1 < len(matrix):
                    self.check_node_and_update(i, j, i+1, j, matrix, stack, not_visited)
                if j + 1 < len(matrix[0]):
                    self.check_node_and_update(i, j, i, j+1, matrix, stack, not_visited)
            else:
                if i > 0 and matrix[i-1][j] < matrix[i][j]:
                    dp[i][j] = max(dp[i][j], dp[i-1][j] + 1)
                if j > 0 and matrix[i][j-1] < matrix[i][j]:
                    dp[i][j] = max(dp[i][j], dp[i][j-1] + 1)
                if i + 1 < len(matrix) and matrix[i+1][j] < matrix[i][j]:
                    dp[i][j] = max(dp[i][j], dp[i+1][j] + 1)
                if j + 1 < len(matrix[0]) and matrix[i][j+1] < matrix[i][j]:
                    dp[i][j] = max(dp[i][j], dp[i][j+1] + 1)
                stack.pop()
                
                max_path = max(max_path, dp[i][j])
        return max_path