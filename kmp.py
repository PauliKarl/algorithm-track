def _getnextarr(pattern):
    nextArr = [0] * (len(pattern)+1)
    nextArr[0]=-1
    i=0
    j=-1
    while i < len(pattern):
        if j==-1 or pattern[i]==pattern[j]:
            i+=1
            j+=1
            nextArr[i]=j
        else:
            j=nextArr[j]
    return nextArr

def kmp(haystack,pattern):
    nextArr = _getnextarr(pattern)
    h = 0
    p = 0
    while h < len(haystack) and p < len(pattern):
        if p==-1 or haystack[h]==pattern[p]:
            p+=1
            h+=1
        else:
            p=nextArr[p]
    if p==len(pattern):
        return h-p
    return -1

def kmp_ex(haystack, pattern):
    nextArr=[0 for i in pattern]
    nextArr[0] = -1
    nextArr.append(0)
    i=0
    j=-1
    for i in range(len(pattern)):
        while j >-1 and pattern[i]!=pattern[j]:
            j=nextArr[j]
        i+=1
        j+=1
        nextArr[i]=j
    
    h=0
    p=0
    while h<len(haystack):
        while p>-1 and pattern[p]!=haystack[h]:
            p=nextArr[p]
        p+=1
        h+=1
        if p==len(pattern):
            return h-len(pattern)
    return -1


y="aaaabbaaa"
x="bba"

print(kmp(y,x))