class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        Q = []
        ans = [0] * k
        available = SortedList(range(k))
        
        for i, (arr, ld) in enumerate(zip(arrival, load)):
            while Q and Q[0][0] <= arr:
                _, s = heappop(Q)
                available.add(s)
                
            if not available:
                continue
                
            target = i % k
            idx = available.bisect_left(target)
            if idx == len(available):
                idx = 0

            p = available[idx]
            available.remove(p)
            
            heappush(Q, (arr + ld, p))
            ans[p] += 1
            
        mx = max(ans)
        return [i for i, count in enumerate(ans) if count == mx]
