class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        
        n=len(nums)

        st=set()
        for i in range(n):
            for j in range(i,n):
                for k in range(j,n):
                    st.add(nums[i]^nums[j]^nums[k])
        return st
