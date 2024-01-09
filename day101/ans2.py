# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        stack1=[]
        stack2=[]

        def dfs(node,stack):
            if not node:
                return False
            if not node.left and not node.right:
                stack.append(node.val)
            dfs(node.left,stack)
            dfs(node.right,stack)
        
        dfs(root1,stack1)
        dfs(root2,stack2)

        return stack1==stack2