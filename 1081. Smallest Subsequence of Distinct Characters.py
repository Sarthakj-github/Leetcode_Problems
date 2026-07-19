class Solution:
    def smallestSubsequence(self, s: str) -> str:
        S=[]
        st=set()

        for i in s[::-1]:
            if i not in st:
                st.add(i)
                S.append(i)
            elif S[-1]>i:
                S.append(i)
            print(i,S)
        print(S)
        ans=''
        while S:
            j=S.pop()
            if j in st:
                ans+=j
                st.remove(j)
        return ans
