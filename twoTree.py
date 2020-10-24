class TreeNode(object):
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

#create-tree by preorder and inorder
def createTree(preorderlist, inorderlist):
    dict_inorder = {}
    for i in range(len(inorderlist)):
        dict_inorder[inorderlist[i]]=i
    return recur(0,0,len(inorderlist)-1,dict_inorder)
def recur(pre_root,left_in_inorder,right_in_inorder,dict_inorder):
    if left_in_inorder>right_in_inorder:return
    i = dict_inorder[preorderlist[pre_root]]
    root = TreeNode(preorderlist[pre_root])
    root.left = recur(pre_root+1,left_in_inorder,i-1,dict_inorder)
    root.right = recur(pre_root+1+i-left_in_inorder,i+1,right_in_inorder,dict_inorder)
    return root
#pre-order
def preorder(root):
    if not root:
        return
    print(root.val)
    preorder(root.left)
    preorder(root.right)
# in-order
def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.val)
    inorder(root.right)
# post-order
def postorder(root):
    if not root:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.val)
    return 
#level-order
def levelorder(root):
    node = [root]
    while len(node)>0:
        n = len(node)
        for i in range(n):
            nodetree = node.pop(0)
            print(nodetree.val)
            if nodetree.left:
                node.append(nodetree.left)
            if nodetree.right:
                node.append(nodetree.right)
    return 

##非递归遍历
def preorder_non_cur(root):
    #标记法, 0:未访问；1:已访问
    stack = []
    stack.append((root,0))
    while len(stack)>0:
        (node,flg) = stack.pop()
        if not node:continue
        if flg ==0:
            ##先进先出，前序根->左->右，这里应该是右->左->根
            stack.append((node.right,0))
            stack.append((node.left,0))
            stack.append((node,1))
        else:
            print(node.val)


def inorder_non_cur(root):
    #标记法, 0:未访问；1:已访问
    stack = []
    stack.append((root,0))
    while len(stack)>0:
        (node,flg) = stack.pop()
        if not node:continue
        if flg ==0:
            stack.append((node.right,0))
            stack.append((node,1))
            stack.append((node.left,0))
        else:
            print(node.val)
def postorder_non_cur(root):
    #标记法, 0:未访问；1:已访问
    stack = []
    stack.append((root,0))
    while len(stack)>0:
        (node,flg) = stack.pop()
        if not node:continue
        if flg ==0:
            ##后序
            stack.append((node,1))
            stack.append((node.right,0))
            
            stack.append((node.left,0))
            
        else:
            print(node.val)


##最小公共祖先
def lowestCommonAncestor(root, p, q):
    if not root or root.val==p or root.val==q:
        return root
    left = lowestCommonAncestor(root.left,p,q)
    right = lowestCommonAncestor(root.right,p,q)
    if not left and not right:return
    if not left:return right
    if not right:return left
    return root

## mirror tree
def Mirror(root):
    if not root:
        return
    root.left, root.right = root.right, root.left
    Mirror(root.left)
    Mirror(root.right)
    return root

##最大深度
def maxDepth( root ):
    # write code here
    if not root:
        return 0
    return 1+max(maxDepth(root.left),maxDepth(root.right))

##二叉树的最大直径
def maxdiameter(root):
    if not root:
        return 0
    l = maxdiameter(root.left)
    r = maxdiameter(root.right)
    dl = maxDepth(root.left)
    dr = maxDepth(root.right)
    return max(max(l,r),dl+dr)


preorderlist = [0,1,3,6,7,2,4,5,8,9]
inorderlist = [6,3,7,1,0,4,2,8,5,9]

roo = createTree(preorderlist,inorderlist)
postorder(roo)
postorder_non_cur(roo)

#p=6
#q=8
#node = lowestCommonAncestor(roo,p,q)
#print(node.val)