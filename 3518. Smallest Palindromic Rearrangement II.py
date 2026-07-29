class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        n = len(s)//2
        d = {}
        for i in range(n):
            d[s[i]] = d.get(s[i],0)+1
        
        log_fact = [0]*(n+1)
        for i in range(1,n+1):
            log_fact[i] = log_fact[i-1] + math.log(i)
        
        log_deno = 0
        for v in d.values():
            log_deno += log_fact[v]
        
        log_mx = log_fact[n] - log_deno
        if math.log(k) > log_mx + 1e-9:   # compare logs directly
            return ""
        
        ans = []
        L = sorted(d.keys())
        while k and L:
            n -= 1
            for idx,i in enumerate(L):
                log_m = log_fact[n] + math.log(d[i]) - log_deno
                if math.log(k) <= log_m + 1e-9:   # compare logs
                    ans.append(i)
                    log_deno -= log_fact[d[i]]
                    d[i] -= 1
                    log_deno += log_fact[d[i]]
                    if d[i] == 0:
                        L.pop(idx)
                    break
                else:
                    k -= round(math.exp(log_m))   # only small enough values converted
        p = ''
        if len(s) % 2:
            p = s[len(s)//2]
        return ''.join(ans) + p + ''.join(ans[::-1])
