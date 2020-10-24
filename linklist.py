# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        #给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
        p1 = head
        p2 = head
        for i in range(n):
            p2=p2.next
            #链表元素刚好等于N的时候，直接删除第一个元素head即可
            if p2==None:
                return p1.next
        while p2.next:
            p1=p1.next
            p2=p2.next
        p1.next = (p1.next).next
        return head
