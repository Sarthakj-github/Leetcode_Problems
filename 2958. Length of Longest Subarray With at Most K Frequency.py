class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        i,j,n=0,0,len(nums)
        d={}
        m=0
        while j<n:
            if nums[j] not in d:
                d[nums[j]]=1
            else:
                if d[nums[j]]==k:
                    while nums[i]!=nums[j]:
                        d[nums[i]]-=1
                        i+=1
                    i+=1
                else:
                    d[nums[j]]+=1
            j+=1
            m=max(m,j-i)

        return m
