class Solution:
    def canAliceWin(self, n: int) -> bool:
        p=False
        k=10
        while n>=k:
            n-=k
            p=not p
            k-=1
        return p
