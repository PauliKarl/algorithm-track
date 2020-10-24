# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
给定一个二叉树，检查它是否是镜像对称的。
"""
class Solution:
    '''
    两个指针递归，左-右/右-左

    '''
    def isSymmetric(self, root: TreeNode) -> bool:
        #中序遍历是对称的
        def check(lp, rp):
            if lp==None and rp==None:
                return True
            elif lp is not None and rp is not None:
                return lp.val==rp.val and check(lp.right,rp.left) and check(lp.left, rp.right)
            else:
                return False 
        return check(root, root)
    
    """
    利用队列迭代
    
    """
    def isSymmetric_iter(self, root):

        qlist = []
        if not root:
            return True
        qlist.append(root.left)
        qlist.append(root.right)

        while len(qlist)>0:
            if not qlist[0] and not qlist[1]:
                qlist.pop(0)
                qlist.pop(0)
                continue
            elif qlist[0] and qlist[1]:
                fp = qlist.pop(0)
                ep = qlist.pop(0)
                if fp.val!=ep.val:
                    return False
                else:
                    qlist.append(fp.right)
                    qlist.append(ep.left)

                    qlist.append(fp.left)
                    qlist.append(ep.right)
            elif not qlist[0] or not qlist[1]:
                return False
        return True