class Solution:
    def reverseBits(self, n: int) -> int:
        new_num = 0
        i = 32
        while(n):
            new_num = new_num << 1
            new_num = new_num | n&1
            n = n >> 1
            i -= 1
        while(i):
            new_num = new_num << 1
            i -= 1
        return new_num