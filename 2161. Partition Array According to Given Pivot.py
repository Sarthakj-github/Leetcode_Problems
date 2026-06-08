class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n=len(nums)
        ans=[0 for _ in range(n)]
        i,j=0,n-1
        for p in nums:
            if p<pivot:
                ans[i]=p
                i+=1
            elif p>pivot:
                ans[j]=p
                j-=1
        for k in range(i,j+1):
            ans[k]=pivot
        
        j+=1
        ans=ans[:j]+ans[j:][::-1]
        return ans
