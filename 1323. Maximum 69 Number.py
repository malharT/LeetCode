class Solution:
    def maximum69Number (self, num: int) -> int:
        ref = 1
        index = None
        while ref < num:
            if (num%(ref*10) - num%(ref))/ref == 6:
                index = ref
            ref = 10*ref
        if index is not None:
            return num + index*3
        else:
            return num