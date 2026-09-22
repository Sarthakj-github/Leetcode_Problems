class SegTree:
    def __init__(self, nums: List[int], k: int):
        self.k = k
        self.n = len(nums)
        s = 1
        while s < self.n:
            s <<= 1
        self.s = s
        self.tree = [([0]*k, 1) for _ in range(2*s)]
        for i in range(self.n):
            a_mod = nums[i] % k
            cnt = [0]*k
            cnt[a_mod] = 1
            self.tree[s+i] = (cnt, a_mod)
        for p in range(s-1,0,-1):
            self.tree[p] = self.merge(self.tree[2*p], self.tree[2*p+1])

    def merge(self, L, R):
        cntL, prodL = L
        cntR, prodR = R
        k = self.k
        cnt = cntL.copy()
        for r, c in enumerate(cntR):
            if c:
                cnt[(prodL*r)%k] += c
        return cnt, (prodL*prodR)%k

    def update(self, idx, val):
        pos = self.s+idx
        a_mod = val%self.k
        cnt = [0]*self.k
        cnt[a_mod] = 1
        self.tree[pos] = (cnt, a_mod)
        pos//=2
        while pos:
            self.tree[pos] = self.merge(self.tree[2*pos], self.tree[2*pos+1])
            pos//=2

    def query(self, l, r):
        l+=self.s; r+=self.s
        cntL, prodL = [0]*self.k, 1
        cntR, prodR = [0]*self.k, 1
        while l<r:
            if l&1:
                cntL, prodL = self.merge((cntL,prodL), self.tree[l])
                l+=1
            if r&1:
                r-=1
                cntR, prodR = self.merge(self.tree[r], (cntR,prodR))
            l//=2; r//=2
        return self.merge((cntL,prodL),(cntR,prodR))


class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        st = SegTree(nums,k)
        res=[]
        for i,v,s,x in queries:
            st.update(i,v)
            cnt,_ = st.query(s,len(nums))
            res.append(cnt[x%k])
        return res
