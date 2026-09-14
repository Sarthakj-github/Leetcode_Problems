class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        bl1x, bl1y, tr1x, tr1y = rec1
        bl2x, bl2y, tr2x, tr2y = rec2

        if bl1x >= tr2x or bl2x >= tr1x:
            return False
            
        if bl1y >= tr2y or bl2y >= tr1y:
            return False  

        return True
