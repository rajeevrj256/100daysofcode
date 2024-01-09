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
        stack=[]
        if not root1 or not root2:
            return False
        stack.append(root1)

        while stack:
            node=stack.pop()
            if not node.left and not node.right:
                stack1.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        stack.clear()
        stack.append(root2)
        while stack:
            node =stack.pop()
            if not node.left and not node.right:
                stack2.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return stack1==stack2
