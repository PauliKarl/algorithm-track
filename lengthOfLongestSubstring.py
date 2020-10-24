class Solution:        
    """
        请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)<2:
            return len(s)
        maxL = 0
        curL = 0
        maxS = []
        for i in s:
            maxS.append(i)
            if i not in maxS:
                curL+=1
            else:
                if maxL<curL:
                    maxL=curL
                idx = maxS.index(i)#返回第一个等于i值得索引
                maxS=maxS[idx+1:]
                curL = len(maxS)
        if maxL<curL:
            maxL=curL
        return maxL