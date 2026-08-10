class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        d = {}
        def trav(i, p):
            if i == 0:
                return p == 1   # if no stones left, the player who just moved wins
            if (i, p) not in d:
                k = 1
                d[(i, p)] = (p == 1)  # default: losing for current player
                while k * k <= i:
                    a = trav(i - k * k, p ^ 1)
                    if p == 0 and a:        # Alice finds a winning move
                        d[(i, p)] = True
                        break
                    elif p == 1 and not a:  # Bob finds a winning move
                        d[(i, p)] = False
                        break
                    k += 1
            return d[(i, p)]
        
        return trav(n, 0)
