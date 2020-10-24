# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#
# 
# @param head ListNode类 
# @return ListNode类
#
##检测链表是否有环，输出环的节点，没有环就输出None
class Solution:
    def detectCycle(self , head ):
        # write code here
        if not head:
            return None
        fp = head
        lp = head
        while True:
            if not fp or not fp.next:
                return None
            fp=fp.next.next
            lp=lp.next
            if fp==lp:
                break
        lp=head
        
        while fp!=lp:
            fp=fp.next
            lp=lp.next
            
        return lp