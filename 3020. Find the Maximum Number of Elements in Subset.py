class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        d = Counter(nums)
        ans = 0

        # Special case for 1's
        if 1 in d:
            c1 = d[1]
            if c1 % 2 == 0:
                c1 -= 1
            ans = max(ans, c1)

        # Try each base > 1
        for x in list(d.keys()):
            if x == 1: 
                continue
            length = 1
            curr = x
            while True:
                if d[curr]==1:
                    break
                curr*=curr
                if curr in d:
                    length += 2
                else:
                    break
            ans = max(ans, length)
        return ans
