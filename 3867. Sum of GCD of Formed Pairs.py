class Solution:
    def gcdSum(self, nums: List[int]) -> int:
        prefixGcd=[]
        n=len(nums)
        mx=nums[0]
        for nm in nums:
            mx=max(mx,nm)
            prefixGcd.append(gcd(mx,nm))
        
        s=0
        i,j=0,n-1
        prefixGcd.sort()
        while i<j:
            s+=gcd(prefixGcd[i],prefixGcd[j])
            i+=1
            j-=1

        return s
