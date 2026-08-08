class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        N, M = len(word1), len(word2)

        R, C = M - 1, 0
        Right = [0] * N
        for i in range(N - 1, -1, -1):
            Right[i] = C
            if R >= 0 and word1[i] == word2[R]:
                R -= 1
                C += 1

        ans = []
        changed = False
        j = 0

        for i in range(N):
            if j >= M:
                break
            if word1[i] == word2[j]:
                ans.append(i)
                j += 1
            elif not changed and Right[i] >= M - 1 - j:
                ans.append(i)
                j += 1
                changed = True

        return ans if j == M else []
