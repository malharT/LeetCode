class Solution:
    def generate(self, numRows: int) -> list:
        triangle = [[1]]
        for i in range(1, numRows):
            row = [triangle[-1][0]]
            for j in range(i-1):
                row.append(triangle[-1][j] + triangle[-1][j+1])
            row.append(triangle[-1][-1])
            triangle.append(row)
        return triangle

S = Solution()
print(S.generate(5))