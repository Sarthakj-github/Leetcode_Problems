# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:

        ans=0
        def trav(root):
            nonlocal ans
            if root==None:
                return (0,0)
            a,b=trav(root.left)
            c,d=trav(root.right)
            x,y=a+c+root.val,b+d+1
            if root.val==(x//y):
                ans+=1
            return (x,y)
        
        trav(root)
        return ans
