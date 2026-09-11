class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        cnt = [0]*10
        for d in digits:
            cnt[d]+=1
        
        res=0
        for num in range(100,1000,2):
            tmp=num
            need=[0]*10
            for _ in range(3):
                need[tmp%10]+=1
                tmp//=10
            ok=True
            for d in range(10):
                if need[d]>cnt[d]:
                    ok=False
                    break
            if ok:
                res+=1
        
        return res
