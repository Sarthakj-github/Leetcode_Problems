class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        
        L=[]
        for i in nums:
            L.append(i*i)
        
        L.sort(reverse=True)
        ans=0
        i,j=0,len(L)-1
        while i<=j:
            ans+=L[i]
            i+=1
            if i<=j:
                ans-=L[j]
                j-=1
        return ans
