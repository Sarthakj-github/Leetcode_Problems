class Trie:
    def __init__(self):
        self.word=None
        self.chr={}
    
class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        root=Trie()
        ans=None
        L=[]
        i=0
        for word in wordsContainer:
            L.append((len(word),i))
            i+=1
        L.sort()
        root.word=L[0][1]
        while L:
            _,i=L.pop()
            temp=root
            w=list(wordsContainer[i])
            while w:
                c=w.pop()
                if c not in temp.chr:
                    temp.chr[c]=Trie()
                temp.chr[c].word=i
                temp=temp.chr[c]
        ans=[]
        for word in wordsQuery:
            w=list(word)
            temp=root
            while w:
                c=w.pop()
                if c not in temp.chr:
                    break
                temp=temp.chr[c]
            ans.append(temp.word)
        return ans
