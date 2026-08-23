class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        sl = sr = ql = qr = 0

        for i in range(n):
            if i < n // 2:
                if num[i] == '?':
                    ql += 1
                else:
                    sl += int(num[i])
            else:
                if num[i] == '?':
                    qr += 1
                else:
                    sr += int(num[i])

        if (ql - qr) == 0:
            return sl != sr

        if (ql + qr) % 2:
            return True

        return 2 * (sl - sr) != 9 * (qr - ql)
