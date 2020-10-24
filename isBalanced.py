# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
给定一个二叉树，判断它是否是高度平衡的二叉树。

本题中，一棵高度平衡二叉树定义为：

一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。
"""
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def hightTree(p):
            if p==None:
                return -1
            return 1+max(hightTree(p.right), hightTree(p.left))
        if root == None:
            return True
        if abs(hightTree(root.right)-hightTree(root.left))>1:
            return False
        else:
            return self.isBalanced(root.right) and self.isBalanced(root.left)