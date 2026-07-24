class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        
        n=len(nums)

        st=set()
        L=[]
        for j in range(0,n):
            for k in range(j,n):
                st.add(nums[j]^nums[k])
        
        St=set()
        for i in range(0,n):
            for p in st:
                St.add(p^nums[i])
    
        return len(St)
