class Solution:
    def test_speed(self, speed, piles):
        total_hours = 0
        for pile in piles:
            hrs = pile//speed
            total_hours += hrs + (pile%speed > 0)
        return total_hours


    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = sum(piles)//float(h)
        low = max(1, int(low) + low > int(low))
        hi = max(piles)+1
        mid = low + (hi-low)//2
        ans = mid
        while hi > low:
            mid = low + (hi-low)//2
            c_h = self.test_speed(mid, piles)
            if h >= c_h:
                ans = mid
                hi = mid
            elif h < c_h:
                low = mid+1
        return ans
