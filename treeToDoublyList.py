"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    """
    输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的循环双向链表。要求不能创建任何新的节点，只能调整树中节点指针的指向
    """
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        """
        中序遍历
        """
        if not root:
            return None      
        nodelist = []
        def recur(root):
            if not root:return
            recur(root.left)
            nodelist.append(root)
            recur(root.right)
        
        recur(root)

        if len(nodelist)==1:
            nodelist[0].left = nodelist[0]
            nodelist[0].right = nodelist[0]
            return nodelist[0]
        for i in range(len(nodelist)):
            nodelist[i].left=nodelist[i-1]
            nodelist[i].right=nodelist[(i+1)%len(nodelist)]
        return nodelist[0]