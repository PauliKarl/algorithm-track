# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
    从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。

    采用BFS， 利用队列的先入先出
    """
    def levelOrderI(self, root: TreeNode) -> List[int]:
        res=[]  #存放结果
        que=[] #实现队列功能
        if not root:
            return []
        que.append(root)
        while que:
            node = que.pop(0)
            res.append(node.val)
            if node.left:
                que.append(node.left)
            if node.right:
                que.append(node.right)
        return res


#class Solution:
    """
    从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。
    """
    def levelOrderII(self, root: TreeNode) -> List[List[int]]:
        res=[]
        que=[]
        if not root:
            return []
        que.append([root])
        while que:
            nodes=que.pop(0)
            tmp = [node.val for node in nodes]
            res.append(tmp)

            tempnodes = []
            for node in nodes:
                if node.left:
                    tempnodes.append(node.left)
                if node.right:
                    tempnodes.append(node.right)
            if tempnodes:
                que.append(tempnodes)
        return res

#class Solution:
    """
    请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。
    """
    def levelOrderIII(self, root: TreeNode) -> List[List[int]]:
        res=[]
        que=[]
        if not root:
            return []
        que.append([root])
        while que:
            nodes=que.pop(0)
            tmp = [node.val for node in nodes]
            res.append(tmp)

            tempnodes = []
            for node in nodes:
                if node.left:
                    tempnodes.append(node.left)
                if node.right:
                    tempnodes.append(node.right)
            if tempnodes:
                que.append(tempnodes)
        for l in range(len(res)):
            if l%2==1:
                res[l].reverse()
        
        return res


