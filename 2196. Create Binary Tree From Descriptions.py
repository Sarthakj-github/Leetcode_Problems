# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        
        d={}
        par={}

        for p,c,l in descriptions:
            if p not in d:
                d[p]=TreeNode(p)
            if c not in d:
                d[c]=TreeNode(c)
            if p not in par:
                par[p]=1
            par[c]=0
            if l:
                d[p].left=d[c]
            else:
                d[p].right=d[c]
        
        for p in par:
            if par[p]:
                return d[p]
