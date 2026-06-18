class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        ans = abs(6*minutes - (hour%12)*30 - minutes/2)
        return min(ans, 360-ans)
