class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        L = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if not (arriveAlice <= arriveBob <= leaveAlice or arriveBob <= arriveAlice <= leaveBob):
            return 0

        ma = max(arriveAlice, arriveBob)
        ml = min(leaveAlice, leaveBob)

        mm, md = map(int, ma.split('-'))
        lm, ld = map(int, ml.split('-'))

        if mm == lm:
            return ld - md + 1

        ans = 0
        for m in range(mm + 1, lm):
            ans += L[m - 1]

        return ans + L[mm - 1] - md + 1 + ld
