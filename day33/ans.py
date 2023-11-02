# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.result=0
    def averageOfSubtree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.dfs(root)
        return self.result

        
    def dfs(self,node):
        if not node:
            return (0,0)
        left_sum,left_count=self.dfs(node.left)
        right_sum,right_count=self.dfs(node.right)

        curr_sum= node.val+left_sum+right_sum
        curr_count=1+left_count+right_count

        if curr_sum//curr_count == node.val:
            self.result +=1

        return (curr_sum,curr_count)
       

        
        
        