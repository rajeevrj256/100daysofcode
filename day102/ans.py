# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        res = 0

        def dfs(node):
            if not node:
                return (0, False)

            l_res,l_found = dfs(node.left)
            r_res,r_found = dfs(node.right)

            if node.val == start:
                nonlocal res
                res = max(res, l_res, r_res)
                return (1,True)

            if l_res == 0 and r_res == 0:
                return (1,False)

            if l_found or r_found:
                res = max(res, l_res+r_res)
            
            if l_found:
                return (l_res+1, True)
            
            if r_found:
                return (r_res+1, True)

            return (max(l_res,r_res)+1, False)

        dfs(root)

        return res