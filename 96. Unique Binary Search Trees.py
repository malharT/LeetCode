class Solution:
    def numTrees(self, n: int) -> int:
        nums = list(range(n))
        dp = [1, 1]
        for i in range(2, n+1):
            dp.append(0)
            for left in range(i):
                right = i-1 - left
                dp[i] += dp[left] * dp[right]
        return dp[-1]

S = Solution()
print(S.numTrees(4))