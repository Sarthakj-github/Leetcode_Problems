class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        s=set()
        ans=set()
        for w in word:
            if w.islower() and w.upper() in s:
                ans.add(w)
            elif w.isupper() and w.lower() in s:
                ans.add(w.lower())
            else:
                s.add(w)
        return len(ans)
