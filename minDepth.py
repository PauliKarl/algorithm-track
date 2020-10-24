"""
广度优先搜索
"""
class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root):
        depth = 0
        
        chlist = []
        chlist.append(root)
        while len(chlist)>0:
            n = len(chlist)
            for i in range(n):
                node = chlist.pop(0)

                if node.left is None and node.right is None:
                    return depth
                if node.left:
                    chlist.append(node.left)
                if node.right:
                    chlist.append(node.right)
            depth+=1
        return depth

