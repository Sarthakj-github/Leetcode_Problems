class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        
        mo,me=float('inf'),float('inf')
        for i in nums1:
            if i%2:
                mo=min(mo,i)
            else:
                me=min(me,i)
        
        if mo==float('inf') or me==float('inf') or mo<=me:
            return True
        
        return False
