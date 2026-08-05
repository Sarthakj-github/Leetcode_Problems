class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        edges = [[] for _ in range(n)]
        in_degree = [0] * n

        for u, v in invocations:
            edges[u].append(v)
            in_degree[v] += 1

        queue = collections.deque([k])
        sus = bytearray(n)
        sus[k] = 1

        while queue:
            u = queue.popleft()
            for v in edges[u]:
                in_degree[v] -= 1
                if sus[v] == 0:
                    sus[v] = 1
                    queue.append(v)

        for i in range(n):
            if sus[i] and in_degree[i] > 0:
                return list(range(n))

        return [i for i in range(n) if sus[i] == 0]
