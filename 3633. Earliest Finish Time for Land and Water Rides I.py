class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:

        n,m=len(landStartTime),len(waterStartTime)

        ans=float('inf')
        for i in range(n):
            for j in range(m):
                if landStartTime[i]<=waterStartTime[j]:
                    k=landStartTime[i]+landDuration[i]
                    if waterStartTime[j]<=k:
                        k+=waterDuration[j]
                    else:
                        k=waterStartTime[j]+waterDuration[j]
                    ans=min(ans,k)
                else:
                    k=waterStartTime[j]+waterDuration[j]
                    if landStartTime[i]<=k:
                        k+=landDuration[i]
                    else:
                        k=landStartTime[i]+landDuration[i]
                    ans=min(ans,k)
        return ans
