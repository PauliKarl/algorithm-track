# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
    输入一棵二叉树和一个整数，打印出二叉树中节点值的和为输入整数的所有路径。从树的根节点开始往下一直到叶节点所经过的节点形成一条路径。
    """
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res=[]
        path=[]

        def recur(root, tar):
            """
            先序遍历+回溯
            """
            if not root: return
            path.append(root.val)
            if tar==root.val and not root.left and not root.right:
                res.append(list(path))
            recur(root.left, tar-root.val)
            recur(root.right, tar-root.val)
            path.pop()
        recur(root, sum)
        return res