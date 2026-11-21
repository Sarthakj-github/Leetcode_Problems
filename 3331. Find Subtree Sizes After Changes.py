class Solution:
  def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
    n = len(parent)
    T = {i: [] for i in range(n)}

    for i in range(n):
      p = parent[i]
      if p not in T:
        T[p] = []
      T[p].append(i)

    d = {}

    def trav(x):
      if s[x] in d and d[s[x]]:
        parent[x] = d[s[x]][-1] 
      d.setdefault(s[x], []).append(x)
      if x in T:
        for c in T[x]:
          trav(c)
      d[s[x]].pop()  

    trav(0)

    T = {i: [] for i in range(n)}
    for i in range(n):
      p = parent[i]
      if p not in T:
        T[p] = []
      T[p].append(i)

    ans = [0 for _ in range(n)]

    def count(x):
      sz = 1  
      for c in T[x]:  
        sz += count(c)
      ans[x] = sz
      return ans[x]

    count(0)

    return ans
