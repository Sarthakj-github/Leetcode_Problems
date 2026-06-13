class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        n = 26
        ans = ''
        for w in words:
            c = 0
            for l in w:
                c += weights[ord(l) - ord('a')]
            # map to a lowercase letter safely
            ans += chr(ord('a') + (25 - (c % n)))
        return ans
