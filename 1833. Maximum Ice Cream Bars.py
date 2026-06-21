class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        c,s=0,0
        for i in costs:
            s+=i
            if s>coins:
                return c
            c+=1
        return c
