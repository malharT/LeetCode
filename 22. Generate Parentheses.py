class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        dp = [['()']]
        for i in range(1,n):
            new_list = []
            strings = set()
            #inside loop
            for j in range(i):
                item_1_1 = dp[j][0][:j+1]
                item_1_2 = dp[j][0][j+1:]
                for item in dp[i-j-1]:
                    new_item = item_1_1 + item + item_1_2
                    if new_item not in strings:
                        new_list.append(new_item)
                        strings.add(new_item)
            for j in range(i):
                for item1 in dp[j]:
                    for item2 in dp[i-j-1]:
                        new_item1 = item2 + item1
                        if new_item1 not in strings:
                            new_list.append(new_item1)
                            strings.add(new_item1)
                        new_item2 = item1 + item2
                        if new_item2 not in strings:
                            new_list.append(new_item2)
                            strings.add(new_item2)
            dp.append(new_list)
        return dp[-1]