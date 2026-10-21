class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        
        # 1. If already sorted, 0 operations needed
        if all(s[i] <= s[i + 1] for i in range(n - 1)):
            return 0
            
        # 2. A length-2 unsorted string cannot be sorted using proper substrings
        if n == 2:
            return -1
            
        mn, mx = min(s), max(s)
        
        # 3. If min is already at the beginning or max is at the end
        if s[0] == mn or s[-1] == mx:
            return 1
        
        # 4. If min or max appears in the interior
        if any(c == mn or c == mx for c in s[1:-1]):
            return 2
            
        # 5. Otherwise, 3 operations are required
        return 3
