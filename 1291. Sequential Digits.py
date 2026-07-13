class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        
        ld,ud=len(str(low)),len(str(high))
        ans=[]
        for l in range(ld,ud+1):
            k=1
            while k<=(10-l):
                p=k
                for _ in range(l-1):
                    p=p*10+(p%10+1)
                if low<=p<=high:
                    ans.append(p)
                k+=1
        return ans
