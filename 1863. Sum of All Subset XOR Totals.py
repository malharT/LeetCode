class Solution:
    def get_positions(self, num):
        positions=[]
        while(num):
            temp_num = num ^ num-1
            positions.append((temp_num+1) >> 1)
            num = num&(num-1)
        return positions

    def subsetXORSum(self, nums: List[int]) -> int:
        s = 0
        self.bin_pos = {}
        for i in range(len(nums)):
            self.bin_pos[1<<i] = i
        for i in range(1, 1 << len(nums)):
            x_s = 0
            p = self.get_positions(i)
            for pos in p:
                pos = self.bin_pos[pos]
                x_s ^= nums[pos]
            s += x_s
        return s
