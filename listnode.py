class ListNode:
    def __init__(self,x=None):
        self.val = x
        self.next = None
##翻转链表
def reverseList(head):
    if not head:
        return head
    pre = None
    cur = head
    nxt = head.next
    while (nxt):
        cur.next = pre
        pre = cur
        cur = nxt
        nxt = nxt.next
    cur.next=pre
    return cur

def printList(head):
    res = []
    while head:
        res.append(head.val)
        head=head.next
    return res

def createList(arr):
    head = ListNode(arr[0])
    arr.pop(0)

    p=head
    for i in range(len(arr)):
        p.next = ListNode(arr[i])
        p = p.next
    return head

#如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序
#k 是一个正整数，它的值小于或等于链表的长度
def reverseKGroup(head,K):
    dummy = ListNode(0)
    dummy.next = head
    pre, end = dummy, dummy
    while end.next:
        for i in range(K):
            if end:
                end = end.next
        if not end:
            break
        start = pre.next
        nxt = end.next
        end.next = None
        pre.next = reverseList(start)
        start.next = nxt
        pre = start
        end = pre
    return dummy.next



head=createList([0,1,2,3,4,5,6,7])
print(printList(reverseKGroup(head,3)))