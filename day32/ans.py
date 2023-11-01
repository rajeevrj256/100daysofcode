# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.curr_count=0
        self.max_count=0
        self.prev_val=None
        self.modes=[]

        def dfs(node):
            if not node:
                return 
            dfs(node.left)
            if node.val!=self.prev_val:
                self.curr_count=1
            else:
                self.curr_count +=1
            if self.curr_count > self.max_count:
                self.max_count=self.curr_count
                self.modes= [node.val]
            elif self.curr_count== self.max_count:
                self.modes.append(node.val)
            self.prev_val=node.val
            dfs(node.right)
        dfs(root)
        return self.modes


        