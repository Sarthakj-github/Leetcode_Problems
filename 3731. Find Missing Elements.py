class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        
        m,M=min(nums),max(nums)
        s=set(nums)
        L=[]

        for i in range(m+1,M):
            if i not in s:
                L.append(i)
        
        return L
