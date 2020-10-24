# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''
输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
'''
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        self.dict_inorder = {}
        self.preorder = preorder
        for i in range(len(inorder)):
            self.dict_inorder[inorder[i]]=i
        return self.recur(0,0,len(inorder)-1)
    def recur(self,pre_root,left_in_inorder,right_in_inorder):
        '''
        arguments
            pre_root: the idx in preorder[list] of root
            left_in_inorder: the idx of the first TreeNode in inorder[list]
            right_in_inorder: the idx of the last TreeNode in inorder[list]
        '''
        if left_in_inorder>right_in_inorder:return #stop recur
        i = self.dict_inorder[self.preorder[pre_root]] # use the root to split the inorder[list]: leftTree+root+rightTree
        root = TreeNode(self.preorder[pre_root]) # build the root Node
        root.left = self.recur(pre_root+1, left_in_inorder, i-1) # build leftTree with recur
        root.right = self.recur(i-left_in_inorder+pre_root+1,i+1,right_in_inorder) # build rightTree with recur
        return root # return the root Node