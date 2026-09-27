class Solution:
    def reverseParentheses(self, s: str) -> str:
        S = ['']
        for ch in s:
            if ch == '(':
                S.append('')
            elif ch == ')':
                t=S.pop()[::-1]
                S[-1]+=t
            else:
                S[-1] += ch
        return ''.join(S)
