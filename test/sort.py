def quick(a):
    if len(a)<2:
        return a
    midval = a[len(a)//2]
    a.pop(len(a)//2)
    left = []
    right = []
    for i in range(len(a)):
        if a[i]<midval:
            left.append(a[i])
        else:
            right.append(a[i])
    return quick(left) + [midval] + quick(right)

#arr = [1,1,2,7,9,9,3,4,5,10,8]
#print(quick(arr)) 

def helper(s):
    left = []
    delidx = []
    for i in range(len(s)):
        if s[i]=="(":
            left.append(i)
        elif s[i]==")" and len(left)>0:
            left.pop()
        elif s[i]==")" and len(left)==0:
            delidx.append(i)
    delidx.extend(left)

    res= ""
    for i in range(len(s)):
        if i not in delidx:
            res = res + s[i]
    return res

st = "((a(s))(d)f)g)h"
print(helper(st))