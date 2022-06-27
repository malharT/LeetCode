class Solution(object):
    def maxCoins(self, nums):
        dp = []
        nums = [1] + nums + [1]
        for _ in range(len(nums)):
            dp.append([0 for _ in range(len(nums))])
        for i in range(2, len(nums)):
            for j in range(i-2, -1, -1):
                for k in range(j+1, i):
                    new_reward = nums[j]*nums[k]*nums[i] + dp[i][k] + dp[k][j]
                    dp[i][j] = max(dp[i][j], new_reward)
        return dp[len(nums)-1][0]