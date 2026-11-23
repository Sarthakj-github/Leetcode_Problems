class ProductOfNumbers:

    def __init__(self):
        self.A=[(1,0)]

    def add(self, num: int) -> None:
        if num==0:
            self.A.append((self.A[-1][0],self.A[-1][1]+1))
        else:
            self.A.append((self.A[-1][0]*num,self.A[-1][1]))

    def getProduct(self, k: int) -> int:
        a,b=self.A[-k-1]
        c,d=self.A[-1]
        if d-b:
            return 0
        return c//a

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
