class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        m,s=0,0
        for i in gain:
            s+=i
            m=max(m,s)
        return m
