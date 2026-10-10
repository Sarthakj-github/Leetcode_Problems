class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        p = k1 + k2
        diffs = [abs(a - b) for a, b in zip(nums1, nums2)]
        if sum(diffs) <= p: 
            return 0
        
        maxd = max(diffs)
        freq = [0] * (maxd + 1)
        for d in diffs:
            freq[d] += 1
        
        for d in range(maxd, 0, -1):
            if not freq[d]: 
                continue
            take = min(p, freq[d])
            freq[d] -= take
            freq[d-1] += take
            p -= take
            if p == 0: 
                break
        
        ans = 0
        for d in range(maxd + 1):
            if freq[d]:
                ans += d * d * freq[d]
        return ans
