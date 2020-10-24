# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    """
    输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)
    B是A的子结构， 即 A中有出现和B相同的结构和节点值。
    """
    def inTree(self,a,b):
        if not b:
            return True
        elif not a or b.val != a.val:
            return False
        return self.inTree(a.left, b.left) and self.inTree(a.right, b.right)
         
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        return bool(A and B) and (self.inTree(A, B) or self.isSubStructure(A.left,B) or self.isSubStructure(A.right,B))