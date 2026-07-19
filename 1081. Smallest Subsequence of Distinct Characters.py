class Solution:
    def smallestSubsequence(self, s: str) -> str:
        last = {c:i for i,c in enumerate(s)}   # last occurrence of each char
        st = []
        used = set()

        for i,c in enumerate(s):
            if c in used:
                continue
            while st and c < st[-1] and last[st[-1]] > i:
                used.remove(st.pop())
            st.append(c)
            used.add(c)
        return ''.join(st)
