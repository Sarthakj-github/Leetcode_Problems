class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        arr = [1 if x==target else -1 for x in nums]
        
        pref = [0]
        for v in arr:
            pref.append(pref[-1]+v)
        
        # coordinate compression
        vals = sorted(set(pref))
        comp = {v:i+1 for i,v in enumerate(vals)}  # 1-indexed for BIT
        
        def add(bit,i):
            while i<len(bit):
                bit[i]+=1
                i+=i&-i
        def sum(bit,i):
            s=0
            while i>0:
                s+=bit[i]
                i-=i&-i
            return s
        
        bit=[0]*(len(vals)+2)
        ans=0
        for p in pref:
            idx=comp[p]
            # count how many previous prefix sums < current
            ans+=sum(bit,idx-1)
            add(bit,idx)
        return ans
