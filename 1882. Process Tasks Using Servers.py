import heapq

class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        free_servers = [(weight, i) for i, weight in enumerate(servers)]
        heapq.heapify(free_servers)
        
        busy_servers = []
        
        ans = [-1] * len(tasks)
        time = 0
        
        for j, task_weight in enumerate(tasks):
            time = max(time, j)
            
            while busy_servers and busy_servers[0][0] <= time:
                _, weight, index = heapq.heappop(busy_servers)
                heapq.heappush(free_servers, (weight, index))
            
            if not free_servers:
                time = busy_servers[0][0]
                while busy_servers and busy_servers[0][0] <= time:
                    _, weight, index = heapq.heappop(busy_servers)
                    heapq.heappush(free_servers, (weight, index))
            
            weight, index = heapq.heappop(free_servers)
            ans[j] = index
            heapq.heappush(busy_servers, (time + task_weight, weight, index))
            
        return ans
