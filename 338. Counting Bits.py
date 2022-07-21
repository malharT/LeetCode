class Solution:
    def countBits(self, n: int) -> List[int]:
        arr = [0]
        next_pow = 1
        for i in range(1,n+1):
            if i == next_pow:
                arr.append(1)
                next_pow = 2*next_pow
            elif i%2 == 1:
                arr.append(arr[-1] + 1)
            else:
                last_pow = int(next_pow/2)
                arr.append(arr[last_pow] + arr[i-last_pow])
        return arr