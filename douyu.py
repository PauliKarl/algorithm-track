# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.res=0
    def recur(self,root,left):
        if not root:
            return
        if not root.left  and not root.right  and left:
            self.res+=root.val
            return
        if root.left==None and root.right==None and not left:
            self.res-=root.val
            return
        self.recur(root.left, True)
        self.recur(root.right, False)
    def leftsubright(self, root):
        #左叶子之和减去右叶子之和
        if root.left:
            self.recur(root.left, True)
        if root.right:
            self.recur(root.right, False)
        return self.res

def subb(num1,num2):
    #大数减法 +/- or ++
    num1 = list(num1)
    num2 = list(num2)
    res = []
    if num1[0]!="-" and num2[0]=="-":
        num2=num2[1:]
        cnt=0
        while len(num1)>0 or len(num2)>0:
            if len(num2)==0:
                s1 = num1.pop()
                if int(s1)+cnt>9:
                    res.insert(0,int(s1)+cnt-10)
                    cnt=1
                else:
                    res.insert(0,int(s1)+cnt)
                    cnt=0
            elif len(num1)==0:
                s2 = num2.pop()
                if int(s2)+cnt>9:
                    res.insert(0,int(s2)+cnt-10)
                    cnt=1
                else:
                    res.insert(0,int(s2)+cnt)
                    cnt=0
            else:
                s1 = num1.pop()
                s2 = num2.pop()
                if int(s1)+int(s2)+cnt>9:
                    res.insert(0,int(s1)+int(s2)+cnt-10)
                    cnt=1
                else:
                    res.insert(0,int(s1)+int(s2)+cnt)
                    cnt=0
        if cnt==1:
            res.insert(0,1)
        r=""
        for i in res:
            r=r+str(i)
        return r

def suba(num1,num2):
    #num1-num2同号相减
    res=""
    cnt=0
    flag = False
    if num1[0]=="-" and num2[0]=="-":
        flag=True
        num1 = num1[1:]
        num2 = num2[1:]

    for i in range(len(num1)):
        if i<len(num2):
            if (int(num1[-(i+1)])-int(num2[-(i+1)])-cnt)<0:
                res=str((10+int(num1[-(i+1)])-int(num2[-(i+1)])-cnt))+res
                cnt=1
            else:
                res=str((int(num1[-(i+1)])-int(num2[-(i+1)])-cnt))+res
                cnt=0
        else:
            if (int(num1[-(i+1)])-cnt)<0:
                res=str((10+int(num1[-(i+1)])-cnt))+res
                cnt=1
            else:
                res=str((int(num1[-(i+1)])-cnt))+res
                cnt=0  
    if flag:
        return "-"+res
    else:
        return res   

num1="565"
num2="567"
print(suba(num1,num2))