class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key=lambda x: (x[0],-x[1]))

        S=[]
        for itv in intervals:
            if S==[]:
                S.append(itv)
            else:
                a,b=S[-1]
                c,d=itv
                if not (a<=c<=d<=b):
                    S.append(itv)
        return len(S)
