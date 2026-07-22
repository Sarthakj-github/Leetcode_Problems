class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        c = s.count('1')

        # build segments
        S = []
        i = 0
        while i < n:
            j = i + 1
            while j < n and s[i] == s[j]:
                j += 1
            S.append((i, j - 1, s[i]))
            i = j
        l = len(S)

        # map positions to segment index
        pos_to_seg = [0] * n
        for idx, (x, y, v) in enumerate(S):
            for j in range(x, y + 1):
                pos_to_seg[j] = idx

        # precompute gains
        gain = [0] * l
        for i in range(1, l - 1):
            if S[i][2] == '1':
                gain[i] = (S[i - 1][1] - S[i - 1][0] + 1) + (S[i + 1][1] - S[i + 1][0] + 1)

        # sparse table for RMQ
        log = [0] * (l + 1)
        for i in range(2, l + 1):
            log[i] = log[i // 2] + 1
        K = log[l] + 1
        st = [[0] * l for _ in range(K)]
        st[0] = gain[:]
        for j in range(1, K):
            for i in range(l - (1 << j) + 1):
                st[j][i] = max(st[j - 1][i], st[j - 1][i + (1 << (j - 1))])

        def query_rmq(L, R):
            if L > R: return 0
            j = log[R - L + 1]
            return max(st[j][L], st[j][R - (1 << j) + 1])

        def eval_seg(idx, L, R, segL, segR):
            if idx <= segL or idx >= segR: return 0
            if S[idx][2] == '0': return 0
            if idx - 1 == segL:
                left_len = max(0, S[idx - 1][1] - L + 1)
            else:
                left_len = S[idx - 1][1] - S[idx - 1][0] + 1
            if idx + 1 == segR:
                right_len = max(0, R - S[idx + 1][0] + 1)
            else:
                right_len = S[idx + 1][1] - S[idx + 1][0] + 1
            return left_len + right_len

        res = []
        for a, b in queries:
            segL, segR = pos_to_seg[a], pos_to_seg[b]
            if segR - segL < 2:
                res.append(c)
                continue
            max_gain = 0
            max_gain = max(max_gain, eval_seg(segL + 1, a, b, segL, segR))
            max_gain = max(max_gain, eval_seg(segR - 1, a, b, segL, segR))
            if segL + 2 <= segR - 2:
                max_gain = max(max_gain, query_rmq(segL + 2, segR - 2))
            res.append(c + max_gain)

        return res
