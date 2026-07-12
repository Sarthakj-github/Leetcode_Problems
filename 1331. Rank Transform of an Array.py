class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        n=len(arr)
        d={}
        for i in range(n):
            a=arr[i]
            if a not in d:
                d[a]=[]
            d[a].append(i)
        
        L=list(d.keys())
        L.sort()

        r=1
        for l in L:
            while d[l]!=[]:
                arr[d[l].pop()]=r
            r+=1
        return arr
