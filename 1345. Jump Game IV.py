class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n=len(arr)
        if n==1:
            return 0
        d={}
        for i in range(n):
            if arr[i] not in d:
                d[arr[i]]=[]
            d[arr[i]].append(i)
        
        Q=[(0,0)]
        S=set()
        S.add(0)
        while Q!=[]:
            a,b = Q.pop(0)
            while d[arr[a]]!=[]:
                p=d[arr[a]].pop()
                if p not in S:
                    if p==(n-1):
                        return b+1
                    else:
                        Q.append((p,b+1))
                        S.add(p)
            if a!=0 and (a-1) not in S:
                Q.append((a-1,b+1))
                S.add(a-1)
            if (a+1) not in S:
                if (a+1)==(n-1):
                    return b+1
                Q.append((a+1,b+1))
                S.add(a+1)
        return False
